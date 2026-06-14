import os

class GenerativeFinancialAgent:
    """
    Simulates and implements an autonomous market researcher using LangChain/OpenAI schemas.
    Accepts mathematical backtest parameters and outputs professional macro briefings.
    """
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

    def generate_market_briefing(self, current_price, predicted_price, current_volatility, mae_metric):
        price_delta = predicted_price - current_price
        direction = "BULLISH" if price_delta > 0 else "BEARISH"
        
        # Formulate structured prompt context (RAG Prompt Template Structure)
        prompt_template = f"""
        ROLE: Senior Macroeconomic Quantitative Strategist
        CONTEXT:
        - Current Asset Value: {current_price} INR
        - Next-Day Model Target Forecast: {predicted_price} INR
        - Trailing Volatility Index: {current_volatility:.2f}
        - Historical Model Error Buffer (MAE): {mae_metric:.2f} INR
        - System Expected Momentum Vector: {direction} (Expected Drift: {price_delta:.2f} INR)
        
        TASK: Synthesize a professional, concise market disclosure and strategic asset allocation advisory text.
        """
        
        if not self.api_key:
            # Fully functional local fallback simulator guaranteeing production compilation 
            return f"[LOCAL AGENT FALLBACK SUMMARY]: The system detects a strong {direction} momentum signal. With trailing volatility holding at {current_volatility:.2f} and an active tracking variance of {mae_metric:.2f} INR, short-term positioning should adjust exposure constraints to accommodate the predicted drift of {price_delta:.2f} INR."
            
        # Production execution block when live API keys are supplied
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key)
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt_template}],
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Gen AI Execution Exception: {e}"

if __name__ == "__main__":
    agent = GenerativeFinancialAgent()
    sample_report = agent.generate_market_briefing(135000, 135771, 245.5, 562.17)
    print("\nGenerated Gen AI Market Briefing Output:")
    print(sample_report)
