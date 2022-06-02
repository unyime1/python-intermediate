-- upgrade --
CREATE TABLE IF NOT EXISTS "follows" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "followee_id" UUID REFERENCES "user" ("id") ON DELETE CASCADE,
    "follower_id" UUID REFERENCES "user" ("id") ON DELETE CASCADE
);
-- downgrade --
DROP TABLE IF EXISTS "follows";
