# Django Blog

A simple blog website built with Django, featuring CRUD operations for blog posts, user authentication, and comments functionality.

## Features

- **Create**: Users can create new blog posts.
- **Read**: View all blog posts and individual post details.
- **Update**: Edit existing blog posts.
- **Delete**: Remove blog posts.
- **Authentication**: User login and registration.
- **Comments**: Users can comment on blog posts.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML (Server-side rendered), Tailwind CSS

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/hafizabdullah1/django-blog-website.git
   ```
   
2. Navigate into the project directory:
   ```
   cd django-blog-website
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Configure your database settings in `settings.py`.
   - Run migrations:
     ```
     python manage.py migrate
     ```

5. Start the server:
   ```
   python manage.py runserver
   ```

6. Access the application in a web browser at `http://localhost:8000` (or another specified port).

## Usage

1. **User Registration and Login**:
   - Navigate to `/signup` to create a new user account.
   - After registration, login at `/login`.

2. **Create Blog Post**:
   - Once logged in, visit `/post/create/` to create a new blog post.

3. **View Blog Posts**:
   - All blog posts are listed on the homepage (`/`).
   - Click on a post title to view its details (`/posts/:slug`).

4. **Update and Delete Blog Post**:
   - While logged in, visit the post detail page (`/posts/:slug`) to edit or delete the post but only author of post can edit or delete the post.

5. **Comments**:
   - Logged-in users can comment on blog posts using the comment form on each post detail page.

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---