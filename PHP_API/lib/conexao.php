<?php
class Conexao extends PDO {

    private $banco = 'gamquiz';
    private $user = 'databaseuser';
    private $pass = 'nicepassword';

    function __construct() {
        $dsn = 'mysql:host=localhost;dbname=' . $this->banco;
        $options = array(
            PDO::ATTR_PERSISTENT => true,
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
        );
        try {
            parent::__construct($dsn, $this->user, $this->pass, $options);
        } catch (PDOException $e) {
            file_put_contents('erros.txt', $e->getMessage() . "\r\n", FILE_APPEND);
            die('Erro no sistema. Tente mais tarde.');
        }
    }
}

