<?php

class Geral{
	public static function getRandom($escolha1){
		$bd = new Conexao();

		if ($escolha1){
			$sql = "SELECT texto, resposta, alt_A, alt_B, alt_C, alt_D, tipo FROM perguntas ORDER BY RAND() LIMIT 5";
		}
		else{
			$sql = "SELECT texto, resposta, alt_A, alt_B, alt_C, alt_D, tipo FROM perguntas WHERE tipo='M' ORDER BY RAND() LIMIT 5";
		}
		$result = $bd->query($sql);
		return $result->fetchAll(PDO::FETCH_OBJ);
	}

	public static function getUpdate(){
		$bd = new Conexao();
		$sql = "SELECT valor FROM versao";
		$result = $bd->query($sql);

		return $result->fetch(PDO::FETCH_NUM);
	}
}
