# Kavya Pingale - Portfolio Website

A dynamic, fully responsive, and highly interactive portfolio website built with HTML, CSS, and Vanilla JavaScript. It features an integrated Admin Dashboard for live content management and Supabase backend for analytics, contact messages, and visitor authentication.

## Features

- **Dynamic Content Management**: Edit profile, skills, projects, certificates, and more directly from a secure Admin Panel.
- **Supabase Integration**:
  - **Contact Form**: Messages are saved directly to the database.
  - **Visitor Analytics**: Tracks page views, unique logged-in visitors, and recent visits.
  - **Visitor Authentication**: Visitors can sign up or log in via Supabase Email Auth.
- **Interactive UI**: Custom cursor, particle background, smooth scrolling, and glassmorphism design.
- **Responsive Design**: Works flawlessly on desktops, tablets, and mobile devices.

## Setup Instructions

### 1. Local Development
1. Clone this repository.
2. Open `index.html` in your browser (or use an extension like Live Server in VS Code).
3. Access the Admin Panel at `/admin-login.html`.

### 2. Supabase Backend Setup
To enable the backend features (Messages, Analytics, and Auth):
1. Create a [Supabase](https://supabase.com/) project.
2. Update the `SUPABASE_URL` and `SUPABASE_KEY` variables in both `index.html` and `admin.html`.
3. Run the following SQL in your Supabase SQL Editor:

```sql
-- Contact Messages Table
CREATE TABLE IF NOT EXISTS contact_messages (
  id BIGSERIAL PRIMARY KEY,
  name TEXT,
  email TEXT,
  subject TEXT,
  message TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
ALTER TABLE contact_messages ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow public inserts" ON contact_messages FOR INSERT TO public WITH CHECK (true);
CREATE POLICY "Allow public reads" ON contact_messages FOR SELECT TO public USING (true);
CREATE POLICY "Allow public deletes" ON contact_messages FOR DELETE TO public USING (true);

-- Page Views / Analytics Table
CREATE TABLE IF NOT EXISTS page_views (
  id BIGSERIAL PRIMARY KEY,
  user_email TEXT,
  path TEXT NOT NULL,
  visited_at TIMESTAMPTZ DEFAULT NOW()
);
ALTER TABLE page_views ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow public inserts on page_views" ON page_views FOR INSERT TO public WITH CHECK (true);
CREATE POLICY "Allow public reads on page_views" ON page_views FOR SELECT TO public USING (true);
```
4. In Supabase, go to **Authentication -> Providers** and enable **Email** auth.

## Deployment to Vercel

This project is a static site (HTML/CSS/JS) and can be deployed to Vercel in seconds.

1. Go to [Vercel](https://vercel.com/) and sign in.
2. Click **Add New -> Project**.
3. Import this GitHub repository.
4. Leave the Framework Preset as `Other` and Build Command / Output Directory empty.
5. Click **Deploy**.

Vercel will automatically host your site and provide you with a live URL!
