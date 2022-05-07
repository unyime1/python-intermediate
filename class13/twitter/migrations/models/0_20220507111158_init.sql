-- upgrade --
CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "username" VARCHAR(50),
    "email" VARCHAR(100),
    "first_name" VARCHAR(100),
    "last_name" VARCHAR(100),
    "last_logged" TIMESTAMPTZ,
    "hashed_password" VARCHAR(1000),
    "phone" VARCHAR(100),
    "day_of_birth" VARCHAR(20),
    "month_of_birth" VARCHAR(20),
    "year_of_birth" VARCHAR(20),
    "email_verified" BOOL   DEFAULT False
);
COMMENT ON TABLE "user" IS 'User table';
CREATE TABLE IF NOT EXISTS "picture" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "url" VARCHAR(500),
    "filename" VARCHAR(200),
    "filesize" VARCHAR(100),
    "user_id" UUID REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "tweet" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "content" VARCHAR(600),
    "user_id" UUID REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "tweet" IS 'User tweet';
CREATE TABLE IF NOT EXISTS "comment" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "content" VARCHAR(600),
    "tweet_id" UUID REFERENCES "tweet" ("id") ON DELETE CASCADE,
    "user_id" UUID REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "comment" IS 'Tweet comment';
CREATE TABLE IF NOT EXISTS "like" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "tweet_id" UUID REFERENCES "tweet" ("id") ON DELETE CASCADE,
    "user_id" UUID REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "like" IS 'Tweet likes';
CREATE TABLE IF NOT EXISTS "media" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "url" VARCHAR(500),
    "filename" VARCHAR(200),
    "filesize" VARCHAR(100),
    "tweet_id" UUID REFERENCES "tweet" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "media" IS 'Tweet media';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
