<?php

require 'lib/conexao.php';
require 'models/Jogador.php';
require 'models/Geral.php';

if (!empty($_POST['username'])){
	$username = $_POST['username'];
}

if (!empty($_POST['token'])){
	$token = $_POST['token'];
}

if (!empty($_POST['opcao'])){
	$opcao = $_POST['opcao'];
}

if (!empty($_POST['escolha1'])){
	$escolha1 = $_POST['escolha1'];
}
else {
	$escolha1 = 0;
}

if (!empty($_POST['escolha2'])){
	$escolha2 = $_POST['escolha2'];
}
else{
	$escolha2 = 0;
}

if (!empty($_POST['senha'])){
	$senha = $_POST['senha'];
}
else {
	$senha = 0;
}
if (!empty($_POST['opcao'])){
	$opcao = $_POST['opcao'];
}

if (!empty($_POST['score'])){
	$score = $_POST['score'];
}

if ($opcao){
	switch($opcao){
		case 1:
			registrar($username, $senha);
			break;
		case 2:
			login($username, $senha);
			break;
		case 3:
			getTop10($escolha1, $escolha2);
			break;
		case 4:
			getColocacao($username, $escolha1, $escolha2);
			break;
		case 5:
			setPontos($username, $token, $score, $escolha1);
			break;
		case 6:
			getRandom($escolha1);
			break;
		case 7:
			getUpdate();
			break;
		case 8:
			getPontos($username, $escolha1);
			break;
		default:
			echo '{"resposta": "CACHORRO"}';
			break;
	}
}

function registrar($username, $senha){
	$j = new Jogador($username);

	if (!$j->username){
		$j = new Jogador();
		$j->username = $username;
		$j->senha = $senha;
		$j->token = '';
		$j->pontos = 0;
		$j->pontos_hoje = 0;
		$j->pontos_matematica = 0;
		$j->p_hoje_matematica = 0;

		$j->save();
		echo '{"resposta": 1}';
	}
	else {
		echo '{"resposta": 0}';
	}
}

function login($username, $senha){
	$j = new Jogador($username);

	if ($j->senha == $senha){
		$resposta = array('token' => $j->login());
		echo  json_encode($resposta);
	}
	else {
		echo '{"token": 0}';
	}
}

function getTop10($escolha1, $escolha2){
	$top10 = Jogador::top10($escolha1, $escolha2);
	echo json_encode($top10);
}

function getColocacao($username, $escolha1, $escolha2){
	$colocacao = Jogador::getColocacao($username, $escolha1, $escolha2);
	echo '{"colocacao": '.$colocacao[0].'}';
}

function setPontos($username, $token, $score, $escolha1){
	$j = new Jogador($username);
	if ($j->token == $token){
		if ($escolha1){
			$pontos = $j->pontos + $score;
			$p_hoje = $j->pontos_hoje + $score;
			$j->pontos = $pontos;
			$j->pontos_hoje = $p_hoje;
			$j->save();
			echo '{"resposta": 1}';
		}
		else {
			$p_matematica = $j->pontos_matematica + $score;
			$p_hoje_m = $j->p_hoje_matematica + $score;
			$j->pontos_matematica = $p_matematica;
			$j->p_hoje_matematica = $p_hoje_m;
			$j->save();
			echo '{"resposta": 1}';
		}
	}
	else{
		echo '{"resposta": 0}';
	}
}

function getRandom($escolha1){
	$respostas = Geral::getRandom($escolha1);

	echo json_encode($respostas);
}

function getUpdate(){
	$versao = Geral::getUpdate()[0];

	echo '{"versao": '.$versao.'}';
}

function getPontos($username, $escolha1){
	$j = new Jogador($username);

	if ($escolha1){
		$todos = $j->pontos;
		$hoje = $j->pontos_hoje;
	}
	else {
		$todos = $j->pontos_matematica;
		$hoje = $j->p_hoje_matematica;
	}
	echo '{"todos": '.$todos.', "hoje": '.$hoje.'}';

}
