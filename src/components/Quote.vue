<template>
    <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
            <v-col cols="12" sm="8" md="4">
                <v-card class="elevation-12">
                    <v-toolbar color="primary" dark flat>
                        <v-img
                            class="shrink mr-5 ml-3"
                            contain
                            src="@/assets/bottle2.png"
                            transition="scale-transition"
                            width="30"
                        />

                        <v-toolbar-title class="font-weight-black">Is it a good day for drinking?</v-toolbar-title>
                        <v-spacer />
                        <v-btn icon color="green" @click="updateIndex" v-if="pressed && quote">
                            <v-icon>mdi-cached</v-icon>
                        </v-btn>
                    </v-toolbar>
                    <v-card-subtitle class="mt-10 mx-2" v-if="pressed && quote">
                        <p
                            class="text-justify font-weight-medium"
                        >Well... It's up for you to decide. Here's what famous people think:</p>
                    </v-card-subtitle>
                    <v-card-text v-if="pressed && !quote" align="center">
                        <v-progress-circular indeterminate color="primary" />
                    </v-card-text>
                    <v-card-text v-if="pressed && quote">
                        <p class="text-justify font-italic mx-2">{{ quote.quote }}</p>
                        <p class="text-right font-weight-bold mx-2">{{ quote.author }}</p>
                    </v-card-text>
                    <v-card-actions v-if="!pressed">
                        <v-flex class="text-center">
                            <v-btn color="primary" @click="pressed = true">Find out</v-btn>
                        </v-flex>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script lang="ts">
import Vue from 'vue';

export interface QuoteInfo {
    quote: string;
    author: string;
    source: string;
}

import { Component, Prop, Watch } from 'vue-property-decorator';

@Component({})
export default class App extends Vue {
    @Prop() private quotes!: QuoteInfo[];

    private pressed: boolean = false;
    private quoteIndex: number = -1;
    @Watch('quotes')
    private onReceiveQuotes() {
        this.updateIndex();
    }

    private get quote(): QuoteInfo | null {
        if (this.quoteIndex !== -1) {
            return this.quotes[this.quoteIndex];
        }
        return null;
    }

    private updateIndex() {
        if (this.quotes && this.quotes.length) {
            this.quoteIndex = Math.round(Math.random() * this.quotes.length);
        }
    }
}

</script>
