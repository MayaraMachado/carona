-- 1 querie
-- Simples, Like, order by

SELECT first_name, date_joined 
	FROM auth_user 
	WHERE last_name ILIKE 'carro'
	ORDER BY date_joined DESC; 

-- 2 querie


SELECT au.first_name, m.cnh FROM public.viagem
	INNER JOIN carro c on carro_idcarro = c.idcarro
	INNER JOIN motorista m on m.idmotorista = c.motorista_idmotorista
	INNER JOIN auth_user au on au.id = m.usuario_idusuario;

-- 3 querie
-- Media de avaliação de motoristas

SELECT * FROM
	(SELECT au.first_name as nome, placa, media FROM
		(SELECT c.placa as placa, avg(a.nota) as media, c.motorista_idmotorista as motorista 
			FROM public.viagem v
			INNER JOIN public.avaliacao a on v.avaliacao_idavaliacao = a.idavaliacao
			INNER JOIN public.carro c on c.idcarro = v.carro_idcarro
			GROUP BY placa, motorista
		) as query1
		INNER JOIN motorista m ON m.idmotorista = motorista
		INNER JOIN public.auth_user au on au.id = m.usuario_idusuario
		GROUP BY nome, placa, media, motorista
	) as query2
	GROUP BY nome, placa, media
	HAVING media >= 5
		



-- 4 querie
-- Listar todas as mensagens da conversa do viagem x




-- 5 querie
--Listar algum calculo




-- 6 querie
-- Listar os carros que fizeram a viagem mais cara que a media das viagens (aninhada)


-- 7 querie
--


-- 8 querie

-- 9 querie

-- 10 querie