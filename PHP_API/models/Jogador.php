<?php

class Jogador{
	public $id;
	public $username;
	public $senha;
	public $token;
	public $pontos;
	public $pontos_hoje;
	public $pontos_matematica;
	public $p_hoje_matematica;

	function __construct($username=NULL){
		if ($username){
			$bd = new Conexao();
			$result = $bd->query("SELECT * FROM jogadores WHERE username='$username'");
			$jogador = $result->fetch(PDO::FETCH_OBJ);

			if (!$jogador){
				return 0;
			}
			foreach ($jogador as $key => $value){
				$this->$key = $value;
			}
		}
	}

	public function save(){
		$bd = new Conexao();
		if ($this->id){
			$sql = 'UPDATE jogadores SET username=:username, token=:token,
			 senha=:senha, pontos=:pontos, pontos_hoje=:pontos_hoje, 
			pontos_matematica=:pontos_matematica, 
			p_hoje_matematica=:p_hoje_matematica WHERE id='.$this->id;
		}
		else {
			$sql = 'INSERT INTO jogadores(username, token, senha, pontos, pontos_hoje, 
				pontos_matematica, p_hoje_matematica) VALUES (:username, 
				:token, :senha, :pontos, :pontos_hoje, :pontos_matematica, 
				:p_hoje_matematica)';
		}
		$stmt = $bd->prepare($sql);
		$stmt->bindParam(':username', $this->username);
		$stmt->bindParam(':token', $this->token);
		$stmt->bindParam(':senha', $this->senha);
		$stmt->bindParam(':pontos', $this->pontos, PDO::PARAM_INT);
		$stmt->bindParam(':pontos_hoje', $this->pontos_hoje, PDO::PARAM_INT);
		$stmt->bindParam(':pontos_matematica', $this->pontos_matematica, PDO::PARAM_INT);
		$stmt->bindParam(':p_hoje_matematica', $this->p_hoje_matematica, PDO::PARAM_INT);
		return $stmt->execute();
	}

	public function login(){
		try{
			$this->token = md5(mt_rand(1, 1000).time());
			$this->save();
			return $this->token;
		}
		catch(Exception $e){
			0;
		}	
	}

	public static function top10($escolha1, $escolha2){
		$bd = new Conexao();
		if ($escolha1){
			if ($escolha2){
				$sql="SELECT username, pontos FROM jogadores ORDER BY pontos DESC LIMIT 10";
			}
			else{
				$sql="SELECT username, pontos_hoje FROM jogadores ORDER BY pontos_hoje DESC LIMIT 10";
			}
		}
		else{
			if ($escolha2){
				$sql="SELECT username, pontos_matematica FROM jogadores ORDER BY pontos_matematica DESC LIMIT 10";
			}
			else{
				$sql="SELECT username, p_hoje_matematica FROM jogadores ORDER BY p_hoje_matematica DESC LIMIT 10";
			}
		}
		$rs = $bd->query($sql);
		return $rs->fetchAll(PDO::FETCH_OBJ);
	}

	public static function getColocacao($username, $escolha1, $escolha2){
		$bd = new Conexao();
                if ($escolha1){
                        if ($escolha2){
                                $sql="SELECT COUNT(*) FROM jogadores WHERE pontos > (SELECT pontos FROM jogadores WHERE username='$username')";
                        }
                        else{
                                $sql="SELECT COUNT(*) FROM jogadores WHERE pontos_hoje > (SELECT pontos_hoje FROM jogadores WHERE username='$username')";

                        }
                }
                else{
                        if ($escolha2){
                                $sql="SELECT COUNT(*) FROM jogadores WHERE pontos_matematica > (SELECT pontos_matematica FROM jogadores WHERE username='$username')";

                        }
                        else{
                                $sql="SELECT COUNT(*) FROM jogadores WHERE p_hoje_matematica > (SELECT p_hoje_matematica FROM jogadores WHERE username='$username')";

                        }
                }
		$rs = $bd->query($sql);
		return $rs->fetchAll(PDO::FETCH_COLUMN, 0);
	}
}
