import React from "react";

const  UserItem = ({user}) => {
    return(
        <tr>
            <td>{user.user_name}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.gender}</td>
            <td>{user.birthday_year}</td>
            <td>{user.email}</td>
        </tr>
    );
};

const  UserList = ({users}) =>{
    return (
        <table>
            <th>Логин</th>
            <th>Имя</th>
            <th>Фамилия</th>
            <th>Пол</th>
            <th>Год рождения</th>
            <th>E-MAIL</th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
};

export default UserList;