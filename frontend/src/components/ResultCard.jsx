import './ResultCard.css'

function ResultCard({ result }) {
    const isSpam = result.prediction === 'spam'
    const confidencePercentage = (result.confidence * 100).toFixed(1)

    return (
        <div className={`result-card fade-in ${isSpam ? 'spam' : 'safe'}`}>
            <div className="result-header">
                <div className="result-icon">
                    {isSpam ? (
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 9V11M12 15H12.01M5.07183 19H18.9282C20.4678 19 21.4301 17.3333 20.6603 16L13.7321 4C12.9623 2.66667 11.0377 2.66667 10.2679 4L3.33975 16C2.56995 17.3333 3.53223 19 5.07183 19Z"
                                stroke="currentColor"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round" />
                        </svg>
                    ) : (
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
                                stroke="currentColor"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round" />
                        </svg>
                    )}
                </div>
                <div className="result-text">
                    <h3 className="result-title">
                        {isSpam ? '⚠️ Spam Detected' : '✅ Safe Email'}
                    </h3>
                    <p className="result-subtitle">
                        {isSpam
                            ? 'This email appears to be spam or potentially malicious'
                            : 'This email appears to be legitimate and safe'
                        }
                    </p>
                </div>
            </div>

            <div className="confidence-section">
                <div className="confidence-header">
                    <span className="confidence-label">Confidence Score</span>
                    <span className="confidence-value">{confidencePercentage}%</span>
                </div>
                <div className="confidence-bar">
                    <div
                        className="confidence-fill"
                        style={{ width: `${confidencePercentage}%` }}
                    />
                </div>
            </div>

            <div className="probabilities-section">
                <h4 className="probabilities-title">Probability Distribution</h4>
                <div className="probabilities-grid">
                    {Object.entries(result.probabilities).map(([label, probability]) => (
                        <div key={label} className="probability-item">
                            <div className="probability-header">
                                <span className="probability-label">
                                    {label === 'spam' ? '🚫 Spam' : '✅ Safe'}
                                </span>
                                <span className="probability-value">
                                    {(probability * 100).toFixed(1)}%
                                </span>
                            </div>
                            <div className="probability-bar">
                                <div
                                    className={`probability-fill ${label}`}
                                    style={{ width: `${probability * 100}%` }}
                                />
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            <div className="result-footer">
                <div className="result-tip">
                    <svg className="tip-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M13 16H12V12H11M12 8H12.01M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
                            stroke="currentColor"
                            strokeWidth="2"
                            strokeLinecap="round"
                            strokeLinejoin="round" />
                    </svg>
                    <span>
                        {isSpam
                            ? 'Avoid clicking links or downloading attachments from spam emails'
                            : 'Always verify sender identity before sharing sensitive information'
                        }
                    </span>
                </div>
            </div>
        </div>
    )
}

export default ResultCard
