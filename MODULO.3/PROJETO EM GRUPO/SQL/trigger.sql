-- 4. Crie um trigger para ser disparado quando o atributo status de um estudante for atualizado e inserir um novo dado em uma tabela de log. 

-- Crie a tabela de log
CREATE TABLE log_status_update (
  `id_log` INT(11) PRIMARY KEY AUTO_INCREMENT,
  `matricula_fk` BIGINT(11) NOT NULL,
  `status_anterior` VARCHAR(100) NOT NULL,
  `status_atual` VARCHAR(100) NOT NULL,
  `data_atualizacao` DATE
);

-- Crie o trigger (AFTER UPDATE)
DELIMITER //
CREATE TRIGGER tr_atualizacao_status
AFTER UPDATE ON avaliacao
FOR EACH ROW
BEGIN
  IF OLD.status <> NEW.status THEN
    INSERT INTO log_status_update (matricula_fk, status_anterior, status_atual, data_atualizacao)
    VALUES (NEW.matricula_aluno_fk, OLD.status, NEW.status, NOW());
  END IF;
END;
//
DELIMITER ;

