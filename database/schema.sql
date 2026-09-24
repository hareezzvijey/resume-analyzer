-- ============================================================
-- AI RESUME ANALYZER
-- MySQL Database Schema
-- ============================================================
--
-- Database:
--     resume_analyzer_db
--
-- Tables:
--     1. resumes
--     2. job_roles
--     3. resume_analyses
--     4. skill_matches
--
-- ============================================================


-- ============================================================
-- DATABASE
-- ============================================================

CREATE DATABASE IF NOT EXISTS resume_analyzer_db;

USE resume_analyzer_db;


-- ============================================================
-- TABLE 1: resumes
-- ============================================================
--
-- Stores uploaded resume information and the text extracted
-- from the uploaded PDF/DOCX file.
--
-- ============================================================

CREATE TABLE IF NOT EXISTS resumes (

    resume_id INT AUTO_INCREMENT PRIMARY KEY,

    file_name VARCHAR(255) NOT NULL,

    file_type VARCHAR(20) NOT NULL,

    extracted_text TEXT NOT NULL,

    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_resume_file_type
        CHECK (file_type IN ('PDF', 'DOCX'))

);


-- ============================================================
-- TABLE 2: job_roles
-- ============================================================
--
-- Stores target job roles and the skills expected for each role.
--
-- required_skills is stored as MySQL JSON.
--
-- Example:
--
-- [
--     "Python",
--     "SQL",
--     "Pandas",
--     "Machine Learning"
-- ]
--
-- ============================================================

CREATE TABLE IF NOT EXISTS job_roles (

    job_role_id INT AUTO_INCREMENT PRIMARY KEY,

    role_name VARCHAR(150) NOT NULL UNIQUE,

    required_skills JSON NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


-- ============================================================
-- TABLE 3: resume_analyses
-- ============================================================
--
-- Stores the AI-generated analysis of a resume for a
-- particular target job role.
--
-- ============================================================

CREATE TABLE IF NOT EXISTS resume_analyses (

    analysis_id INT AUTO_INCREMENT PRIMARY KEY,

    resume_id INT NOT NULL,

    job_role_id INT NOT NULL,

    overall_score DECIMAL(5,2) NOT NULL,

    skills JSON NOT NULL,

    strengths JSON NOT NULL,

    weaknesses JSON NOT NULL,

    suggestions JSON NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


    -- Resume relationship
    CONSTRAINT fk_analysis_resume
        FOREIGN KEY (resume_id)
        REFERENCES resumes(resume_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,


    -- Job role relationship
    CONSTRAINT fk_analysis_job_role
        FOREIGN KEY (job_role_id)
        REFERENCES job_roles(job_role_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,


    -- Score must be between 0 and 100
    CONSTRAINT chk_overall_score
        CHECK (
            overall_score >= 0
            AND overall_score <= 100
        )

);


-- ============================================================
-- TABLE 4: skill_matches
-- ============================================================
--
-- Stores deterministic job-skill matching results for an
-- individual resume analysis.
--
-- ============================================================

CREATE TABLE IF NOT EXISTS skill_matches (

    match_id INT AUTO_INCREMENT PRIMARY KEY,

    analysis_id INT NOT NULL,

    matched_skills JSON NOT NULL,

    missing_skills JSON NOT NULL,

    match_percentage DECIMAL(5,2) NOT NULL,


    -- Each analysis has one matching result
    CONSTRAINT uq_skill_match_analysis
        UNIQUE (analysis_id),


    -- Analysis relationship
    CONSTRAINT fk_skill_match_analysis
        FOREIGN KEY (analysis_id)
        REFERENCES resume_analyses(analysis_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,


    -- Match percentage must be between 0 and 100
    CONSTRAINT chk_match_percentage
        CHECK (
            match_percentage >= 0
            AND match_percentage <= 100
        )

);


-- ============================================================
-- INDEXES
-- ============================================================
--
-- These are small useful indexes for the MVP.
--
-- ============================================================

CREATE INDEX idx_resumes_uploaded_at
    ON resumes(uploaded_at);

CREATE INDEX idx_analyses_resume_id
    ON resume_analyses(resume_id);

CREATE INDEX idx_analyses_job_role_id
    ON resume_analyses(job_role_id);
