--Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
SELECT * FROM tasks WHERE user_id = 1;

--Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
SELECT * FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name = 'new');

--Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;

--Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

--Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New Task', 'Description', (SELECT id FROM status WHERE name = 'new'), 1);

--Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

--Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
DELETE FROM tasks WHERE id = 1;

--Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
SELECT * FROM users WHERE email LIKE '%@example.com';

--Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
UPDATE users SET fullname = 'New Name' WHERE id = 2;

--Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
SELECT status_id, COUNT(*) FROM tasks GROUP BY status_id;

--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
SELECT * FROM tasks JOIN users ON tasks.user_id = users.id WHERE users.email LIKE '%@example.com';

--Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
SELECT * FROM tasks WHERE description IS NULL;

--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
SELECT * FROM tasks JOIN users ON tasks.user_id = users.id WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress');

--Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
SELECT users.id, users.fullname, COUNT(tasks.id) FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.id;