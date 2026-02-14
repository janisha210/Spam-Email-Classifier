import { useState } from 'react'
import './App.css'
import SpamClassifier from './components/SpamClassifier'
import Header from './components/Header'
import Footer from './components/Footer'

function App() {
    return (
        <div className="app">
            <Header />
            <main className="main-content">
                <SpamClassifier />
            </main>
            <Footer />
        </div>
    )
}

export default App
