<template>
    <v-app>
        <v-content>
            <Quote :quotes="quotes"/>
        </v-content>
    </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import Quote, { QuoteInfo } from './components/Quote.vue';
import { Bucket } from '@google-cloud/storage';
import firebase from 'firebase';
import axios from 'axios';

@Component({
    components: {
        Quote,
    },
})
export default class App extends Vue {
    private quotes: QuoteInfo[] | null = null;
    private mounted() {
        firebase.initializeApp({
            apiKey: 'AIzaSyCxi3ZX6j9R_nBj6lIo2wsPLnwYJOMhseE',
            authDomain: 'drink-quotes.firebaseapp.com',
            databaseURL: 'https://drink-quotes.firebaseio.com',
            projectId: 'drink-quotes',
            storageBucket: 'drink-quotes.appspot.com',
            messagingSenderId: '487939553400',
            appId: '1:487939553400:web:149bf2de9be6d47b9f158d',
            measurementId: 'G-KFV125E8KH',
        });

        firebase.storage().refFromURL('gs://drink-quotes.appspot.com/quotes.json')
            .getDownloadURL().then((downloadUrl) => {
                axios.get(downloadUrl).then((response) => {
                    this.quotes = response.data;
                });
            });
    }
}
</script>
