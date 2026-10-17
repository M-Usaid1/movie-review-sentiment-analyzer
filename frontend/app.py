
# import requests
# import streamlit as st

# API_URL = "http://127.0.0.1:8000/predict"

# st.set_page_config(
#     page_title="Movie Sentiment Analyzer",
#     page_icon="🎬",
#     layout="centered",
# )

# st.title("🎬 Movie Review Sentiment Analyzer")
# st.write(
#     "Powered by your fine-tuned DistilBERT model. "
#     "Enter a movie review to predict its sentiment."
# )

# st.divider()

# review = st.text_area(
#     "Enter your movie review",
#     placeholder="Example: The acting was excellent, and the story kept me engaged...",
#     height=180,
#     max_chars=10000,
# )

# analyze = st.button("Analyze Sentiment", type="primary", use_container_width=True)

# if analyze:
#     if not review.strip():
#         st.warning("Please enter a movie review first.")
#     else:
#         try:
#             with st.spinner("Analyzing your review..."):
#                 response = requests.post(
#                     API_URL,
#                     json={"review": review},
#                     timeout=120,
#                 )

#             if response.status_code == 200:
#                 result = response.json()

#                 sentiment = result["sentiment"]
#                 confidence = result["confidence"]
#                 positive = result["positive_probability"]
#                 negative = result["negative_probability"]

#                 st.subheader("Prediction")

#                 if sentiment == "Positive":
#                     st.success(f"Positive sentiment — {confidence:.1%} confidence")
#                 else:
#                     st.error(f"Negative sentiment — {confidence:.1%} confidence")

#                 col1, col2 = st.columns(2)

#                 with col1:
#                     st.metric("Positive probability", f"{positive:.1%}")

#                 with col2:
#                     st.metric("Negative probability", f"{negative:.1%}")

#                 st.caption(
#                     "Confidence represents the model's predicted probability, "
#                     "not a guarantee that the prediction is correct."
#                 )

#             else:
#                 st.error(f"API error ({response.status_code}): {response.text}")

#         except requests.exceptions.ConnectionError:
#             st.error(
#                 "Cannot connect to the API. Start FastAPI in another terminal "
#                 "using: python -m uvicorn backend.main:app --reload"
#             )

#         except requests.exceptions.Timeout:
#             st.error("The prediction took too long. Please try again.")

#         except requests.exceptions.RequestException as error:
#             st.error(f"Request failed: {error}")

# import requests
# import streamlit as st

# API_URL = "http://127.0.0.1:8000/predict"

# st.set_page_config(
#     page_title="Sentiment AI | Movie Review Analyzer",
#     page_icon="🎬",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ---------- Custom styling ----------
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background: linear-gradient(135deg, #101827 0%, #172554 100%);
#         color: #F8FAFC;
#     }

#     .block-container {
#         max-width: 1100px;
#         padding-top: 2.5rem;
#         padding-bottom: 3rem;
#     }

#     .hero {
#         padding: 2rem 0 1.3rem 0;
#     }

#     .eyebrow {
#         color: #93C5FD;
#         font-size: 0.85rem;
#         font-weight: 700;
#         letter-spacing: 2px;
#         text-transform: uppercase;
#     }

#     .hero h1 {
#         color: #FFFFFF;
#         font-size: clamp(2rem, 5vw, 3.4rem);
#         font-weight: 800;
#         line-height: 1.15;
#         margin: 0.6rem 0;
#     }

#     .hero p {
#         color: #CBD5E1;
#         font-size: 1.08rem;
#         max-width: 720px;
#         line-height: 1.7;
#     }

#     .panel {
#         background: rgba(255, 255, 255, 0.06);
#         border: 1px solid rgba(255, 255, 255, 0.14);
#         border-radius: 18px;
#         padding: 1.35rem;
#         margin-bottom: 1rem;
#     }

#     .result-title {
#         color: #FFFFFF;
#         font-size: 1.5rem;
#         font-weight: 750;
#     }

#     .muted {
#         color: #CBD5E1;
#         font-size: 0.95rem;
#     }

#     div.stButton > button {
#         border-radius: 10px;
#         min-height: 2.8rem;
#         font-weight: 650;
#     }

#     div[data-testid="stTextArea"] textarea {
#         border-radius: 12px;
#     }

#     footer {
#         visibility: hidden;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # ---------- Header ----------
# st.markdown(
#     """
#     <div class="hero">
#         <div class="eyebrow">NLP · TRANSFORMERS · DEEP LEARNING</div>
#         <h1>Movie Review<br>Sentiment Analyzer</h1>
#         <p>
#             Explore the sentiment behind a movie review using a fine-tuned
#             DistilBERT model, served through FastAPI.
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# st.divider()

# # ---------- Sample reviews ----------
# samples = {
#     "Positive example": (
#         "A wonderful film with outstanding performances, "
#         "a compelling story, and a memorable ending."
#     ),
#     "Negative example": (
#         "A disappointing movie with a predictable plot, "
#         "weak performances, and painfully slow pacing."
#     ),
#     "Mixed example": (
#         "The acting was excellent, but the story was slow "
#         "and the ending felt disappointing."
#     ),
# }

# left, right = st.columns([1.15, 0.85], gap="large")

# with left:
#     st.markdown("### Analyze a review")
#     st.markdown(
#         '<p class="muted">Enter your own review or choose an example.</p>',
#         unsafe_allow_html=True,
#     )

#     selected_sample = st.selectbox(
#         "Try a sample",
#         ["Write my own review"] + list(samples.keys()),
#     )

#     default_review = samples.get(selected_sample, "")

#     review = st.text_area(
#         "Movie review",
#         value=default_review,
#         placeholder="What did you think of the movie?",
#         height=220,
#         max_chars=10000,
#         label_visibility="collapsed",
#         key="review_input",
#     )

#     col_analyze, col_clear = st.columns(2)

#     with col_analyze:
#         analyze = st.button(
#             "Analyze sentiment",
#             type="primary",
#             use_container_width=True,
#         )

#     with col_clear:
#         clear = st.button(
#             "Clear review",
#             use_container_width=True,
#         )

#     if clear:
#         st.session_state["review_input"] = ""
#         st.rerun()

# with right:
#     st.markdown("### Prediction")
#     st.markdown(
#         '<div class="panel">',
#         unsafe_allow_html=True,
#     )

#     if analyze:
#         if not review.strip():
#             st.warning("Please enter a review first.")
#         else:
#             try:
#                 with st.spinner("Analyzing review with DistilBERT..."):
#                     response = requests.post(
#                         API_URL,
#                         json={"review": review.strip()},
#                         timeout=120,
#                     )

#                 if response.ok:
#                     result = response.json()

#                     sentiment = result["sentiment"]
#                     confidence = result["confidence"]
#                     positive = result["positive_probability"]
#                     negative = result["negative_probability"]

#                     if sentiment == "Positive":
#                         st.success("😊 Positive sentiment")
#                     else:
#                         st.error("☹️ Negative sentiment")

#                     st.metric(
#                         "Prediction confidence",
#                         f"{confidence:.1%}",
#                     )

#                     st.markdown("**Positive probability**")
#                     st.progress(max(0.0, min(1.0, positive)))
#                     st.caption(f"{positive:.1%}")

#                     st.markdown("**Negative probability**")
#                     st.progress(max(0.0, min(1.0, negative)))
#                     st.caption(f"{negative:.1%}")

#                     st.caption(
#                         "Probabilities reflect the model's output; "
#                         "they are not a guarantee of correctness."
#                     )
#                 else:
#                     st.error(
#                         f"API returned {response.status_code}: "
#                         f"{response.text[:500]}"
#                     )

#             except requests.exceptions.ConnectionError:
#                 st.error(
#                     "Cannot connect to FastAPI. Start the backend "
#                     "in another terminal and try again."
#                 )

#             except requests.exceptions.Timeout:
#                 st.error(
#                     "The prediction timed out. Please try again."
#                 )

#             except (requests.exceptions.RequestException, ValueError, KeyError) as error:
#                 st.error(f"Could not process the prediction: {error}")

#     else:
#         st.markdown(
#             '<div class="result-title">Ready to analyze</div>',
#             unsafe_allow_html=True,
#         )
#         st.markdown(
#             '<p class="muted">Your prediction and probability '
#             'scores will appear here.</p>',
#             unsafe_allow_html=True,
#         )
#         st.markdown("**Model:** Fine-tuned DistilBERT")
#         st.markdown("**Backend:** FastAPI")
#         st.markdown("**Interface:** Streamlit")

#     st.markdown("</div>", unsafe_allow_html=True)

# # ---------- Footer ----------
# st.divider()
# st.markdown(
#     """
#     <p style="text-align:center; color:#CBD5E1; font-size:0.85rem;">
#         Built with Python · PyTorch · Hugging Face Transformers ·
#         FastAPI · Streamlit
#     </p>
#     """,
#     unsafe_allow_html=True,
# )

# import requests
# import streamlit as st

# API_URL = "http://127.0.0.1:8000/predict"

# st.set_page_config(
#     page_title="Sentiment AI | Movie Review Analyzer",
#     page_icon="🎬",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ---------- Sample reviews ----------
# SAMPLES = {
#     "Positive example": (
#         "A wonderful film with outstanding performances, "
#         "a compelling story, and a memorable ending."
#     ),
#     "Negative example": (
#         "A disappointing movie with a predictable plot, "
#         "weak performances, and painfully slow pacing."
#     ),
#     "Mixed example": (
#         "The acting was excellent, but the story was slow "
#         "and the ending felt disappointing."
#     ),
# }


# # ---------- Sample and clear callbacks ----------
# def load_sample():
#     selected = st.session_state["sample_choice"]

#     if selected == "Write my own review":
#         st.session_state["review_input"] = ""
#     else:
#         st.session_state["review_input"] = SAMPLES[selected]


# def clear_review():
#     st.session_state["review_input"] = ""
#     st.session_state["sample_choice"] = "Write my own review"


# # Initialize widget state before rendering widgets.
# if "sample_choice" not in st.session_state:
#     st.session_state["sample_choice"] = "Write my own review"

# if "review_input" not in st.session_state:
#     st.session_state["review_input"] = ""


# # ---------- Custom styling ----------
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background: linear-gradient(135deg, #101827 0%, #172554 100%);
#         color: #F8FAFC;
#     }

#     .block-container {
#         max-width: 1100px;
#         padding-top: 2.5rem;
#         padding-bottom: 3rem;
#     }

#     .hero {
#         padding: 2rem 0 1.3rem 0;
#     }

#     .eyebrow {
#         color: #93C5FD;
#         font-size: 0.85rem;
#         font-weight: 700;
#         letter-spacing: 2px;
#         text-transform: uppercase;
#     }

#     .hero h1 {
#         color: #FFFFFF;
#         font-size: clamp(2rem, 5vw, 3.4rem);
#         font-weight: 800;
#         line-height: 1.15;
#         margin: 0.6rem 0;
#     }

#     .hero p {
#         color: #CBD5E1;
#         font-size: 1.08rem;
#         max-width: 720px;
#         line-height: 1.7;
#     }

#     .panel {
#         background: rgba(255, 255, 255, 0.06);
#         border: 1px solid rgba(255, 255, 255, 0.14);
#         border-radius: 18px;
#         padding: 1.35rem;
#         margin-bottom: 1rem;
#     }

#     .result-title {
#         color: #FFFFFF;
#         font-size: 1.5rem;
#         font-weight: 750;
#     }

#     .muted {
#         color: #CBD5E1;
#         font-size: 0.95rem;
#     }

#     div.stButton > button {
#         border-radius: 10px;
#         min-height: 2.8rem;
#         font-weight: 650;
#     }

#     div[data-testid="stTextArea"] textarea {
#         border-radius: 12px;
#     }

#     footer {
#         visibility: hidden;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


# # ---------- Header ----------
# st.markdown(
#     """
#     <div class="hero">
#         <div class="eyebrow">NLP · TRANSFORMERS · DEEP LEARNING</div>
#         <h1>Movie Review<br>Sentiment Analyzer</h1>
#         <p>
#             Explore the sentiment behind a movie review using a fine-tuned
#             DistilBERT model, served through FastAPI.
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# st.divider()


# # ---------- Main layout ----------
# left, right = st.columns([1.15, 0.85], gap="large")

# with left:
#     st.markdown("### Analyze a review")
#     st.markdown(
#         '<p class="muted">Enter your own review or choose an example.</p>',
#         unsafe_allow_html=True,
#     )

#     st.selectbox(
#         "Try a sample",
#         ["Write my own review"] + list(SAMPLES.keys()),
#         key="sample_choice",
#         on_change=load_sample,
#     )

#     review = st.text_area(
#         "Movie review",
#         placeholder="What did you think of the movie?",
#         height=220,
#         max_chars=10000,
#         label_visibility="collapsed",
#         key="review_input",
#     )

#     col_analyze, col_clear = st.columns(2)

#     with col_analyze:
#         analyze = st.button(
#             "Analyze sentiment",
#             type="primary",
#             use_container_width=True,
#         )

#     with col_clear:
#         st.button(
#             "Clear review",
#             use_container_width=True,
#             on_click=clear_review,
#         )


# with right:
#     st.markdown("### Prediction")

#     with st.container(border=True):
#         if analyze:
#             if not review.strip():
#                 st.warning("Please enter a review first.")
#             else:
#                 try:
#                     with st.spinner("Analyzing review with DistilBERT..."):
#                         response = requests.post(
#                             API_URL,
#                             json={"review": review.strip()},
#                             timeout=120,
#                         )

#                     if response.ok:
#                         result = response.json()

#                         sentiment = result["sentiment"]
#                         confidence = result["confidence"]
#                         positive = result["positive_probability"]
#                         negative = result["negative_probability"]

#                         if sentiment == "Positive":
#                             st.success("😊 Positive sentiment")
#                         else:
#                             st.error("☹️ Negative sentiment")

#                         st.metric(
#                             "Prediction confidence",
#                             f"{confidence:.1%}",
#                         )

#                         st.markdown("**Positive probability**")
#                         st.progress(max(0.0, min(1.0, positive)))
#                         st.caption(f"{positive:.1%}")

#                         st.markdown("**Negative probability**")
#                         st.progress(max(0.0, min(1.0, negative)))
#                         st.caption(f"{negative:.1%}")

#                         st.caption(
#                             "Probabilities reflect the model's output "
#                             "and do not guarantee correctness."
#                         )
#                     else:
#                         st.error(
#                             f"API error ({response.status_code}): "
#                             f"{response.text[:500]}"
#                         )

#                 except requests.exceptions.ConnectionError:
#                     st.error(
#                         "Cannot connect to FastAPI. Keep the backend "
#                         "running in another terminal."
#                     )

#                 except requests.exceptions.Timeout:
#                     st.error(
#                         "The prediction timed out. Please try again."
#                     )

#                 except requests.exceptions.RequestException as error:
#                     st.error(f"Request failed: {error}")

#                 except (ValueError, KeyError) as error:
#                     st.error(f"Could not process the API response: {error}")

#         else:
#             st.markdown(
#                 '<div class="result-title">Ready to analyze</div>',
#                 unsafe_allow_html=True,
#             )
#             st.markdown(
#                 '<p class="muted">Your prediction and probability '
#                 'scores will appear here.</p>',
#                 unsafe_allow_html=True,
#             )
#             st.markdown("**Model:** Fine-tuned DistilBERT")
#             st.markdown("**Backend:** FastAPI")
#             st.markdown("**Interface:** Streamlit")


# # ---------- Footer ----------
# st.divider()

# st.markdown(
#     """
#     <p style="text-align:center; color:#CBD5E1; font-size:0.85rem;">
#         Built with Python · PyTorch · Hugging Face Transformers ·
#         FastAPI · Streamlit
#     </p>
#     """,
#     unsafe_allow_html=True,
# )

import torch
import streamlit as st
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
)

# ==================================================
# 1. CONFIGURATION
# ==================================================

MODEL_REPO = "Usaid2/distilbert-imdb-sentiment"
MODEL_SUBFOLDER = "backend/distilbert_model"

DEVICE = torch.device("cpu")
MAX_LENGTH = 256

# ==================================================
# 2. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Sentiment AI | Movie Review Analyzer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==================================================
# 3. SAMPLE REVIEWS
# ==================================================

SAMPLES = {
    "Positive example": (
        "A wonderful film with outstanding performances, "
        "a compelling story, and a memorable ending."
    ),
    "Negative example": (
        "A disappointing movie with a predictable plot, "
        "weak performances, and painfully slow pacing."
    ),
    "Mixed example": (
        "The acting was excellent, but the story was slow "
        "and the ending felt disappointing."
    ),
}

# ==================================================
# 4. MODEL LOADING
# ==================================================

@st.cache_resource(show_spinner="Loading DistilBERT model...")
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_REPO,
        subfolder=MODEL_SUBFOLDER,
        use_fast=True,
    )

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_REPO,
        subfolder=MODEL_SUBFOLDER,
    )

    model.to(DEVICE)
    model.eval()

    return tokenizer, model


# ==================================================
# 5. SESSION STATE AND CALLBACKS
# ==================================================

if "sample_choice" not in st.session_state:
    st.session_state["sample_choice"] = "Write my own review"

if "review_input" not in st.session_state:
    st.session_state["review_input"] = ""

if "prediction" not in st.session_state:
    st.session_state["prediction"] = None


def load_sample():
    """Load the selected example into the review field."""
    selected = st.session_state["sample_choice"]

    if selected in SAMPLES:
        st.session_state["review_input"] = SAMPLES[selected]
    else:
        st.session_state["review_input"] = ""

    st.session_state["prediction"] = None


def clear_review():
    """Clear the review and reset the selected example."""
    st.session_state["review_input"] = ""
    st.session_state["sample_choice"] = "Write my own review"
    st.session_state["prediction"] = None


# ==================================================
# 6. CUSTOM STYLING
# ==================================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            135deg,
            #101827 0%,
            #172554 100%
        );
        color: #F8FAFC;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    .hero {
        padding: 2rem 0 1.3rem 0;
    }

    .eyebrow {
        color: #93C5FD;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .hero h1 {
        color: #FFFFFF;
        font-size: clamp(2rem, 5vw, 3.4rem);
        font-weight: 800;
        line-height: 1.15;
        margin: 0.6rem 0;
    }

    .hero p {
        color: #CBD5E1;
        font-size: 1.08rem;
        max-width: 720px;
        line-height: 1.7;
    }

    .muted {
        color: #CBD5E1;
        font-size: 0.95rem;
    }

    .result-title {
        color: #FFFFFF;
        font-size: 1.5rem;
        font-weight: 750;
    }

    div.stButton > button {
        border-radius: 10px;
        min-height: 2.8rem;
        font-weight: 650;
    }

    div[data-testid="stTextArea"] textarea {
        border-radius: 12px;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==================================================
# 7. HEADER
# ==================================================

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">
            NLP · TRANSFORMERS · DEEP LEARNING
        </div>

        <h1>
            Movie Review<br>
            Sentiment Analyzer
        </h1>

        <p>
            Explore the sentiment behind a movie review using
            a fine-tuned DistilBERT model hosted on Hugging Face.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ==================================================
# 8. MAIN LAYOUT
# ==================================================

left, right = st.columns(
    [1.15, 0.85],
    gap="large",
)

with left:
    st.markdown("### Analyze a review")

    st.markdown(
        '<p class="muted">'
        'Enter your own review or choose an example.'
        '</p>',
        unsafe_allow_html=True,
    )

    st.selectbox(
        "Try a sample",
        options=[
            "Write my own review",
            *SAMPLES.keys(),
        ],
        key="sample_choice",
        on_change=load_sample,
    )

    st.text_area(
        "Movie review",
        placeholder="What did you think of the movie?",
        height=220,
        max_chars=10000,
        label_visibility="collapsed",
        key="review_input",
    )

    col_analyze, col_clear = st.columns(2)

    with col_analyze:
        analyze = st.button(
            "Analyze sentiment",
            type="primary",
            use_container_width=True,
        )

    with col_clear:
        st.button(
            "Clear review",
            use_container_width=True,
            on_click=clear_review,
        )

# ==================================================
# 9. PREDICTION PANEL
# ==================================================

with right:
    st.markdown("### Prediction")

    with st.container(border=True):

        if analyze:
            review = st.session_state["review_input"].strip()

            if not review:
                st.warning("Please enter a movie review first.")
                st.session_state["prediction"] = None

            else:
                try:
                    with st.spinner(
                        "Loading model and analyzing review..."
                    ):
                        tokenizer, model = load_model()

                        inputs = tokenizer(
                            review,
                            return_tensors="pt",
                            truncation=True,
                            max_length=MAX_LENGTH,
                        )

                        inputs = {
                            name: tensor.to(DEVICE)
                            for name, tensor in inputs.items()
                        }

                        with torch.inference_mode():
                            outputs = model(**inputs)

                            probabilities = torch.softmax(
                                outputs.logits,
                                dim=-1,
                            )[0]

                        if len(probabilities) != 2:
                            raise ValueError(
                                "Expected a binary classification model "
                                "with positive and negative classes."
                            )

                        # Read the model's configured label names.
                        id2label = model.config.id2label

                        label_names = {
                            int(index): str(label).lower()
                            for index, label in id2label.items()
                        }

                        positive_index = next(
                            (
                                index
                                for index, label in label_names.items()
                                if "positive" in label
                            ),
                            1,
                        )

                        negative_index = next(
                            (
                                index
                                for index, label in label_names.items()
                                if "negative" in label
                            ),
                            0,
                        )

                        if (
                            positive_index == negative_index
                            or positive_index not in (0, 1)
                            or negative_index not in (0, 1)
                        ):
                            raise ValueError(
                                "Could not determine the positive and "
                                "negative class indices from the model "
                                "configuration. Check config.json."
                            )

                        predicted_index = int(
                            torch.argmax(probabilities).item()
                        )

                        sentiment = (
                            "Positive"
                            if predicted_index == positive_index
                            else "Negative"
                        )

                        confidence = float(
                            probabilities[predicted_index].item()
                        )

                        positive_probability = float(
                            probabilities[positive_index].item()
                        )

                        negative_probability = float(
                            probabilities[negative_index].item()
                        )

                        st.session_state["prediction"] = {
                            "sentiment": sentiment,
                            "confidence": confidence,
                            "positive": positive_probability,
                            "negative": negative_probability,
                        }

                except Exception as error:
                    st.session_state["prediction"] = None

                    st.error(
                        "Model loading or prediction failed."
                    )

                    with st.expander("Technical error details"):
                        st.code(str(error))

        # Show the most recent successful prediction.
        result = st.session_state["prediction"]

        if result is not None:

            st.divider()

            if result["sentiment"] == "Positive":
                st.success("😊 Positive sentiment")
            else:
                st.error("☹️ Negative sentiment")

            st.metric(
                "Prediction confidence",
                f'{result["confidence"]:.1%}',
            )

            st.markdown("**Positive probability**")

            st.progress(result["positive"])

            st.caption(
                f'{result["positive"]:.1%}'
            )

            st.markdown("**Negative probability**")

            st.progress(result["negative"])

            st.caption(
                f'{result["negative"]:.1%}'
            )

            st.caption(
                "Probabilities reflect the model's estimates, "
                "not a guarantee of correctness."
            )

        elif not analyze:
            st.markdown(
                '<div class="result-title">'
                'Ready to analyze'
                '</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<p class="muted">'
                'Your prediction and probability scores will appear here.'
                '</p>',
                unsafe_allow_html=True,
            )

            st.markdown("**Model:** Fine-tuned DistilBERT")
            st.markdown("**Model hosting:** Hugging Face")
            st.markdown("**Interface:** Streamlit")

# ==================================================
# 10. FOOTER
# ==================================================

st.divider()

st.markdown(
    """
    <p style="
        text-align: center;
        color: #CBD5E1;
        font-size: 0.85rem;
    ">
        Built with Python · PyTorch · Hugging Face Transformers · Streamlit
        <br>
        Predictions may be incorrect, particularly for sarcasm
        and mixed sentiment.
    </p>
    """,
    unsafe_allow_html=True,
)


