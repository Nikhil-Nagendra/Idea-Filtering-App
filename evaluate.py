st.title("Idea Filtering App")

text_input = st.text_area("Enter your idea", height=200)

if st.button("Analyse",key="filter_button"):
    if not text_input:
        st.warning("Please provide your idea for filtering.")
    else:
        feasibility_keywords = ["feasible", "practical", "viable", "workable", "achievable", "realistic", "feasibility", "practicable", "attainable", "doable", "possible", "sensible", "reasonable", "viable", "plausible", "pragmatic", "logical", "conceivable", "manageable", "operable", "appropriate", "fitting", "admissible", "acceptable", "appropriate", "usable", "potential", "capable", "likely", "feasibly"]
        maturity_keywords = ["mature", "established", "developed", "grown", "evolved", "seasoned", "experienced", "settled", "ripe", "fully-grown", "fully-developed", "fully-fledged", "adult", "sophisticated", "well-established", "accomplished", "veteran", "cultivated", "proficient", "skilled", "wise", "knowledgeable", "educated", "trained", "competent", "qualified", "experienced", "seasoned", "practiced", "expert"]
        circular_economy_keywords = ["sustainability", "environment", "recycle", "reuse", "renewable", "green", "ecofriendly", "conservation", "eco-conscious", "sustainable", "earth-friendly", "environmentally-friendly", "low-carbon", "biodegradable", "clean", "organic", "eco-aware", "planet-friendly", "green energy", "renewable resources", "ecological", "ecosystem", "carbon footprint", "green practices", "environmental impact", "ecological balance", "resource conservation", "sustainable development", "eco-friendly"]
        innovativeness_keywords = ["innovative", "novel", "original", "creative", "inventive", "ingenious", "unique", "groundbreaking", "pioneering", "cutting-edge", "forward-thinking", "modern", "visionary", "imaginative", "fresh", "imaginative", "inspired", "innovational", "inventive", "state-of-the-art", "advanced", "ingenious", "revolutionary", "new", "ingenious", "clever", "resourceful", "experimental", "imaginative", "ingenious"]
        market_potential_keywords = ["market potential", "growth potential", "market demand", "opportunity", "market size", "market trends", "business opportunity", "customer demand", "industry demand", "market analysis", "market research", "market saturation", "market niche", "target market", "market segmentation", "market expansion", "market penetration", "market competition", "market feasibility", "economic potential", "financial potential", "business potential", "market needs", "market outlook", "market assessment", "market attractiveness", "market viability", "market prospects", "market dynamics"]

        # Count occurrences of keywords for each criterion
        feasibility_count = sum(text_input.lower().count(keyword) for keyword in feasibility_keywords)
        maturity_count = sum(text_input.lower().count(keyword) for keyword in maturity_keywords)
        circular_economy_count = sum(text_input.lower().count(keyword) for keyword in circular_economy_keywords)
        innovativeness_count = sum(text_input.lower().count(keyword) for keyword in innovativeness_keywords)
        market_potential_count = sum(text_input.lower().count(keyword) for keyword in market_potential_keywords)
        
        
        # Display filtering results based on keyword occurrences
        st.markdown("## Filtering Results")
        st.write(f"Feasibility: {feasibility_count}/30")
        st.write(f"Maturity: {maturity_count}/30")
        st.write(f"Circular Economy: {circular_economy_count}/30")
        st.write(f"Innovativeness: {innovativeness_count}/30")
        st.write(f"Market Potential: {market_potential_count}/30")

