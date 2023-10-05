from fastapi import status
from httpx import AsyncClient, Response

from src.config import config
from src.smtp import smtp_server


class TestMail:
    tested_url = '/api/send_email'

    async def test__when__get_method__then__error_not_allowed(
        self,
        client: AsyncClient,
    ):
        response: Response = await client.get(self.tested_url)

        expected_status = status.HTTP_405_METHOD_NOT_ALLOWED
        real_status = response.status_code

        assert expected_status == real_status

    async def test__when__put_method__then__error_not_allowed(
        self,
        client: AsyncClient,
    ):
        response: Response = await client.put(self.tested_url, data={})

        expected_status = status.HTTP_405_METHOD_NOT_ALLOWED
        real_status = response.status_code

        assert expected_status == real_status

    async def test__when__patch_method__then__error_not_allowed(
        self,
        client: AsyncClient,
    ):
        response: Response = await client.patch(self.tested_url, data={})

        expected_status = status.HTTP_405_METHOD_NOT_ALLOWED
        real_status = response.status_code

        assert expected_status == real_status

    async def test__when__delete_method__then__error_not_allowed(
        self,
        client: AsyncClient,
    ):
        response: Response = await client.delete(self.tested_url)

        expected_status = status.HTTP_405_METHOD_NOT_ALLOWED
        real_status = response.status_code

        assert expected_status == real_status

    async def test__when__post_with_not_valid_data__then__error_bad_request(
        self,
        client: AsyncClient,
    ):
        response: Response = await client.post(self.tested_url, json={})

        expected_status = status.HTTP_422_UNPROCESSABLE_ENTITY
        real_status = response.status_code

        expected_data = {
            'detail': [
                {
                    'input': {},
                    'loc': ['body', 'to'],
                    'msg': 'Field required',
                    'type': 'missing',
                    'url': 'https://errors.pydantic.dev/2.4/v/missing',
                },
                {
                    'input': {},
                    'loc': ['body', 'subject'],
                    'msg': 'Field required',
                    'type': 'missing',
                    'url': 'https://errors.pydantic.dev/2.4/v/missing',
                },
                {
                    'input': {},
                    'loc': ['body', 'message'],
                    'msg': 'Field required',
                    'type': 'missing',
                    'url': 'https://errors.pydantic.dev/2.4/v/missing',
                },
            ],
        }
        real_data = response.json()

        assert expected_status == real_status
        assert expected_data == real_data

    async def test__when__post_with_valid_data__then__return_data(
        self,
        client: AsyncClient,
    ):
        data = {
            'to': 'to',
            'subject': 'subject',
            'message': 'message',
        }

        response: Response = await client.post(self.tested_url, json=data)

        expected_status = status.HTTP_422_UNPROCESSABLE_ENTITY
        real_status = response.status_code

        expected_data = {
            'detail': [
                {
                    'ctx': {
                        'reason': ''.join(
                            (
                                'The email address is not valid. It must ',
                                'have exactly one @-sign.',
                            ),
                        ),
                    },
                    'input': 'to',
                    'loc': ['body', 'to'],
                    'msg': ''.join(
                        (
                            'value is not a valid email address: The email ',
                            'address is not valid. It must have exactly one ',
                            '@-sign.',
                        ),
                    ),
                    'type': 'value_error',
                },
            ],
        }
        real_data = response.json()

        assert expected_status == real_status
        assert expected_data == real_data

    async def test__when__post_with_valid_data__then__error_bad_request(
        self,
        client: AsyncClient,
    ):
        data = {
            'to': 'email@email.email',
            'subject': 'subject',
            'message': 'message',
        }

        with smtp_server.record_messages() as mails:
            response: Response = await client.post(self.tested_url, json=data)

            [mail] = mails

        expected_status = status.HTTP_201_CREATED
        real_status = response.status_code

        expected_data = {
            'detail': 'Email sent.',
        }
        real_data = response.json()

        expected_from = config.MAIL_FROM
        real_from = mail.get('from')

        expected_to = data.get('to')
        real_to = mail.get('to')

        expected_subject = data.get('subject')
        real_subject = mail.get('subject')

        assert expected_status == real_status
        assert expected_data == real_data
        assert expected_from == real_from
        assert expected_to == real_to
        assert expected_subject == real_subject
