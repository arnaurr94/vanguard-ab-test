create database if not exists vanguard;
use vanguard;

drop table session;
CREATE TABLE `session` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `client_id` bigint NOT NULL,
  `visitor_id` text NOT NULL,
  `visit_id` text NOT NULL,
  `process_step` text NOT NULL,
  `date_time` datetime NOT NULL
);

drop table participant;
CREATE TABLE `participant` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `client_id` bigint UNIQUE NOT NULL,
  `variation` text NOT NULL
);

drop table client;
CREATE TABLE `client` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `client_id` bigint UNIQUE,
  `tenure_yr` double DEFAULT null,
  `tenure_months` double DEFAULT null,
  `age` double DEFAULT null,
  `gender` text,
  `num_accounts` double DEFAULT null,
  `balance` double DEFAULT null,
  `calls_6_months` double DEFAULT null,
  `logins_6_months` double DEFAULT null
);


ALTER TABLE `participant` ADD FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`);

ALTER TABLE `session` ADD FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`);