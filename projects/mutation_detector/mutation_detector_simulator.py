import streamlit as st
import math
import base64

# --- hide Streamlit default UI elements ---
st.markdown("""
<style>

/* Hide Streamlit header */
header {
    visibility: hidden;
}

/* Hide the hamburger menu + footer */
#MainMenu {
    visibility: hidden;
}
footer {
    visibility: hidden;
}

/* Remove top spacing created by header */
[data-testid="stAppViewContainer"] {
    margin-top: -60px;
}

</style>
""", unsafe_allow_html=True)

# --- load local image ---
def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("/Users/xkzhao/Learn2Code/projects/genomics_computation/DNA_Background.jpeg")

st.markdown(f"""
<style>

/* page background */
.stApp {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* center entire app */
[data-testid="stAppViewContainer"] {{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}}

/* glass panel */
[data-testid="stAppViewContainer"] .block-container {{
    background: rgba(0,0,0,0.55);
    backdrop-filter: blur(12px);
    padding: 3rem;
    border-radius: 20px;
    max-width: 850px;
    margin: auto;
    margin-top: 60px;
    box-shadow: 0 0 40px rgba(0,0,0,0.6);
}}

h1, h2, h3, p, label {{
    color: white;
}}

</style>
""", unsafe_allow_html=True)

st.title("Mutation Detector")
st.write("Estimate the probability that observed mutations are real.")

# ---- INPUT: n ----
col1, col2 = st.columns([3,1])

with col1:
    n_slider = st.slider("Total sequencing reads (n)", 10, 200, 50)

with col2:
    n_box = st.number_input(" ", min_value=10, max_value=200, value=n_slider)

n = n_box


# ---- INPUT: k ----
col3, col4 = st.columns([3,1])

with col3:
    k_slider = st.slider("Observed mutations (k)", 0, n, 5)

with col4:
    k_box = st.number_input("  ", min_value=0, max_value=n, value=k_slider)

k = k_box


# ---- MODEL PARAMETERS ----
p = 0.001
f = 0.3
prior = 0.001


def binomial_prob(n, k, prob):
    return math.comb(n, k) * (prob**k) * ((1-prob)**(n-k))


P_k_given_M = binomial_prob(n, k, f)
P_k_given_noM = binomial_prob(n, k, p)

posterior = (P_k_given_M * prior) / (
    P_k_given_M * prior + P_k_given_noM * (1 - prior)
)

st.subheader("Result")

st.write(f"Mutation fraction: **{k/n:.3f}**")
st.write(f"Probability mutation is real: **{posterior:.6f}**")

if posterior > 0.95:
    st.success("Very strong evidence for a real mutation.")
elif posterior > 0.5:
    st.warning("Mutation likely real.")
else:
    st.error("Likely sequencing noise.")


st.markdown("### Project Explanation")

st.markdown(
"""
<div style="
height:300px;
overflow-y:auto;
padding:20px;
border-radius:10px;
background: rgba(0,0,0,0.35);
">

<h4>Model Overview</h4>

This project estimates the probability that an observed mutation in sequencing data is real rather than sequencing noise.

We model sequencing reads as a binomial random variable. If the mutation is real, a fraction f of reads will show the mutation. If the mutation is not real, sequencing machines produce errors with probability p.

Using Bayes' theorem, we compute:

P(Mutation | Observed Data)

which combines the likelihood of observing k mutations out of n reads under both hypotheses.

<h4>Why this matters</h4>

Modern cancer genomics pipelines must distinguish real driver mutations from sequencing noise. This probabilistic framework demonstrates how statistical inference can help identify likely real mutations.

</div>
""",
unsafe_allow_html=True
)

