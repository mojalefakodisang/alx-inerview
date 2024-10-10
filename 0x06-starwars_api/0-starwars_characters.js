#!/usr/bin/node
;
const args = process.argv[2];
const api = "https://swapi-api.alx-tools.com/api/people/";

const url = api + args;

const StarWarAPI = async () => {
    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error('Request was not okay: ' + response.statusText);
        }

        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error:', error);
    }
};

StarWarAPI();