import { useState } from 'react'
import './SpamClassifier.css'
import ResultCard from './ResultCard'
import LoadingSpinner from './LoadingSpinner'

function SpamClassifier() {
    const [emailText, setEmailText] = useState('')
    const [loading, setLoading] = useState(false)
    const [result, setResult] = useState(null)
    const [error, setError] = useState(null)

    const handleSubmit = async (e) => {
        e.preventDefault()

        if (!emailText.trim()) {
            setError('Please enter some email text to analyze')
            return
        }

        setLoading(true)
        setError(null)
        setResult(null)

        try {
            // In production (Vercel), use relative path which is handled by vercel.json rewrites
            // In development, default to localhost:8000
            const API_URL = import.meta.env.VITE_API_URL || (import.meta.env.PROD ? '' : 'http://localhost:8000')
            const response = await fetch(`${API_URL}/api/predict`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: emailText }),
            })

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`)
            }

            const data = await response.json()
            setResult(data)
        } catch (err) {
            setError(
                'Failed to analyze email. Please ensure the backend server is running on http://localhost:8000'
            )
            console.error('Error:', err)
        } finally {
            setLoading(false)
        }
    }

    const handleClear = () => {
        setEmailText('')
        setResult(null)
        setError(null)
    }

    const sampleEmails = [
        {
            label: 'Spam Example',
            text: 'CONGRATULATIONS! You have won $1,000,000! Click here NOW to claim your prize before it expires!'
        },
        {
            label: 'Safe Example',
            text: 'Hi team, just a reminder that our project meeting is scheduled for tomorrow at 2 PM. Please review the attached documents beforehand.'
        }
    ]

    const loadSample = (text) => {
        setEmailText(text)
        setResult(null)
        setError(null)
    }

    return (
        <div className="classifier-container">
            <div className="classifier-card">
                <div className="card-header">
                    <h2 className="card-title">Email Spam Detector</h2>
                    <p className="card-description">
                        Paste your email content below and let our AI-powered classifier determine if it's spam or safe
                    </p>
                </div>

                <form onSubmit={handleSubmit} className="classifier-form">
                    <div className="form-group">
                        <label htmlFor="email-input" className="form-label">
                            Email Content
                        </label>
                        <textarea
                            id="email-input"
                            className="email-textarea"
                            placeholder="Paste your email content here..."
                            value={emailText}
                            onChange={(e) => setEmailText(e.target.value)}
                            rows={8}
                            disabled={loading}
                        />
                        <div className="character-count">
                            {emailText.length} characters
                        </div>
                    </div>

                    <div className="sample-buttons">
                        <span className="sample-label">Try a sample:</span>
                        {sampleEmails.map((sample, index) => (
                            <button
                                key={index}
                                type="button"
                                className="sample-button"
                                onClick={() => loadSample(sample.text)}
                                disabled={loading}
                            >
                                {sample.label}
                            </button>
                        ))}
                    </div>

                    <div className="action-buttons">
                        <button
                            type="submit"
                            className="btn btn-primary"
                            disabled={loading || !emailText.trim()}
                        >
                            {loading ? (
                                <>
                                    <LoadingSpinner size="small" />
                                    <span>Analyzing...</span>
                                </>
                            ) : (
                                <>
                                    <svg className="btn-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
                                            stroke="currentColor"
                                            strokeWidth="2"
                                            strokeLinecap="round"
                                            strokeLinejoin="round" />
                                    </svg>
                                    <span>Analyze Email</span>
                                </>
                            )}
                        </button>

                        <button
                            type="button"
                            className="btn btn-secondary"
                            onClick={handleClear}
                            disabled={loading}
                        >
                            <svg className="btn-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M6 18L18 6M6 6L18 18"
                                    stroke="currentColor"
                                    strokeWidth="2"
                                    strokeLinecap="round"
                                    strokeLinejoin="round" />
                            </svg>
                            <span>Clear</span>
                        </button>
                    </div>
                </form>

                {error && (
                    <div className="error-message fade-in">
                        <svg className="error-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 8V12M12 16H12.01M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
                                stroke="currentColor"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round" />
                        </svg>
                        <span>{error}</span>
                    </div>
                )}

                {result && <ResultCard result={result} />}
            </div>

            <div className="info-cards">
                <div className="info-card fade-in">
                    <div className="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M13 10V3L4 14H11L11 21L20 10L13 10Z"
                                stroke="currentColor"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round" />
                        </svg>
                    </div>
                    <h3>Fast & Accurate</h3>
                    <p>Powered by TF-IDF and Naive Bayes machine learning algorithms</p>
                </div>

                <div className="info-card fade-in" style={{ animationDelay: '0.1s' }}>
                    <div className="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 15V3M12 15L8 11M12 15L16 11M2 17L2.621 19.485C2.72915 19.9177 2.97882 20.3018 3.33033 20.5763C3.68184 20.8508 4.11501 20.9999 4.561 21H19.439C19.885 20.9999 20.3182 20.8508 20.6697 20.5763C21.0212 20.3018 21.2708 19.9177 21.379 19.485L22 17"
                                stroke="currentColor"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round" />
                        </svg>
                    </div>
                    <h3>Privacy First</h3>
                    <p>All processing happens locally. Your emails are never stored</p>
                </div>

                <div className="info-card fade-in" style={{ animationDelay: '0.2s' }}>
                    <div className="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M9 12L11 14L15 10M20.618 5.984C20.9474 6.61064 21.1461 7.29846 21.2015 8.00567C21.2568 8.71287 21.1675 9.42381 20.9391 10.0945C20.7108 10.7651 20.3482 11.3818 19.8734 11.9068C19.3986 12.4318 18.8216 12.8541 18.178 13.147L12 16.5L5.822 13.147C5.17838 12.8541 4.60138 12.4318 4.12659 11.9068C3.65179 11.3818 3.28921 10.7651 3.06087 10.0945C2.83253 9.42381 2.74316 8.71287 2.79853 8.00567C2.8539 7.29846 3.05258 6.61064 3.382 5.984L4 4.5L12 8L20 4.5L20.618 5.984Z"
                                stroke="currentColor"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round" />
                        </svg>
                    </div>
                    <h3>Real-time Results</h3>
                    <p>Get instant classification with confidence scores and probabilities</p>
                </div>
            </div>
        </div>
    )
}

export default SpamClassifier
