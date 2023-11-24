"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from models import Base, async_engine, Session, User, Post
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data


async def create_users(
        session: AsyncSession,
        users: List[dict],
):
    users = [User(username=username, name=name, email=email) for user in users for username, name, email in user.items()]
    session.add_all(users)
    await session.commit()


async def create_posts(
        session: AsyncSession,
        posts: List[dict],
):
    posts = [Post(user_id=userID, title=title, body=body) for userID, title, body in posts]
    session.add_all(posts)
    await session.commit()


async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data()
    )
    async with Session() as session:
        async with session.begin():
            for user in users_data:
                session.add(User(id=user['id'], name=user['name'], username=user['username'], email=user['email']))
            for post in posts_data:
                session.add(Post(id=post['id'], user_id=post['userId'], title=post['title'], body=post['body']))

    await async_engine.dispose()


def main():
    pass


if __name__ == "__main__":
    asyncio.run((async_main()))
