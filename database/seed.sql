-- ============================================================
-- AI RESUME ANALYZER
-- MySQL Seed Data
-- ============================================================

USE resume_analyzer_db;


-- ============================================================
-- JOB ROLES
-- ============================================================
--
-- Initial roles for the Job Matching module.
--
-- ============================================================


INSERT INTO job_roles
    (role_name, required_skills)
VALUES

(
    'Data Scientist',

    JSON_ARRAY(
        'Python',
        'SQL',
        'Pandas',
        'NumPy',
        'Machine Learning',
        'Statistics',
        'Scikit-learn'
    )
),


(
    'Machine Learning Engineer',

    JSON_ARRAY(
        'Python',
        'Machine Learning',
        'TensorFlow',
        'PyTorch',
        'Scikit-learn',
        'Docker',
        'Git'
    )
),


(
    'Software Developer',

    JSON_ARRAY(
        'Python',
        'Java',
        'C++',
        'SQL',
        'Git',
        'REST API',
        'Data Structures'
    )
),


(
    'Data Analyst',

    JSON_ARRAY(
        'Python',
        'SQL',
        'Excel',
        'Pandas',
        'NumPy',
        'Data Visualization',
        'Statistics'
    )
);


-- ============================================================
-- VERIFY SEEDED ROLES
-- ============================================================

SELECT
    job_role_id,
    role_name,
    required_skills,
    created_at
FROM job_roles
ORDER BY job_role_id;