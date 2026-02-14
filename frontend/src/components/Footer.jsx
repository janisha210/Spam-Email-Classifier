import './Footer.css'

function Footer() {
    const currentYear = new Date().getFullYear()

    return (
        <footer className="footer">
            <div className="container footer-content">
                <p className="footer-text">
                    Built with <span className="heart">♥</span> using FastAPI & React
                </p>
                <p className="footer-copyright">
                    © {currentYear} Spam Classifier. Powered by Machine Learning.
                </p>
            </div>
        </footer>
    )
}

export default Footer
