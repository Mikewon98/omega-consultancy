DROP TABLE Reviews;
DROP TABLE Banks;

CREATE TABLE Banks (
    bank_id NUMBER GENERATED AS IDENTITY,
    bank_name VARCHAR2(255) NOT NULL UNIQUE,
    PRIMARY KEY(bank_id)
);

CREATE TABLE Reviews (
    review_id NUMBER GENERATED AS IDENTITY,
    bank_id NUMBER,
    review_text CLOB,
    rating NUMBER(2),
    review_date DATE,
    source VARCHAR2(100),
    PRIMARY KEY(review_id),
    CONSTRAINT fk_bank
        FOREIGN KEY (bank_id)
        REFERENCES Banks(bank_id)
);