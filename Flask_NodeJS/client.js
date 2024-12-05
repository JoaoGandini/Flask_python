/**
 * @file client.js
 * @description O script consulta um serviço web para calcular números primos em um intervalo especificado.
 * Usa a biblioteca Axios para realizar requisições HTTP à API Flask, que está rodando localmente.
 * 
 * @dependencies axios - Biblioteca para realizar requisições HTTP.
 */

// Importa a biblioteca axios para realizar requisições HTTP 
const axios = require('axios');
/**
 * @function primos
 * @description Faz uma requisição à API local para buscar números primos em um intervalo.
 * @param {number} limiteInferior - O limite inferior do intervalo.
 * @param {number} limiteSuperior - O limite superior do intervalo.
 * 
 * A função utiliza `axios.get` para realizar uma requisição HTTP GET ao endpoint `/primos`
 * da API local no endereço `http://127.0.0.1:5000/primos`. Envia os limites do intervalo como parâmetros
 * de consulta e tem o resultado exibido no console.
 */
async function primos(limiteInferior, limiteSuperior) {
    try {
        // Faz uma requisição GET para a API Flask
        const response = await axios.get('http://127.0.0.1:5000/primos', {
            params: {
                limite_inferior: limiteInferior, // Envia o limite inferior como parâmetro
                limite_superior: limiteSuperior  // Envia o limite superior como parâmetro
            }
        });
        // Verifica se a resposta HTTP é bem-sucedida (código 200)
        if (response.status === 200) {
            // Exibe os números primos retornados pela API
            console.log("Números primos no intervalo:", response.data.primos);
        } else {
            // Caso a resposta tenha outro código, exibe a mensagem de erro
            console.error("Erro:", response.data.erro);
        }
    } catch (error) {
        // Captura erros na execução da requisição
        if (error.response) {
            // Caso o erro seja uma resposta da API (ex.: erro 400 ou 500)
            console.error("Erro na resposta:", error.response.data.erro);
        } else {
            // Caso o erro seja um problema de rede ou configuração
            console.error("Erro na requisição:", error.message);
        }
    }
}

// Exemplo de teste da função
// Faz uma consulta à API para encontrar os números primos no intervalo de 1 a 100
primos(1, 100);
