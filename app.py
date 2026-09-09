import streamlit as st


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="SeqSense",
    page_icon="🧬",
    layout="wide",
)


# ---------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------

st.title("🧬 SeqSense")

st.subheader("Clinical Bioinformatics FYA Revision")

st.write(
    """
    Welcome to SeqSense — an interactive revision platform
    designed to help prepare for the Clinical Bioinformatics
    Final Year Assessment.
    """
)

st.divider()


# ---------------------------------------------------------
# WELCOME
# ---------------------------------------------------------

st.header("Welcome!")

st.markdown(
    """
    Use SeqSense to revise key areas of clinical bioinformatics,
    test your knowledge and practise applying your knowledge to
    clinical scenarios.

    ### What can you do?

    📚 **Revision**  
    Work through core clinical bioinformatics topics.

    🧠 **Quiz**  
    Test your knowledge with topic-specific questions.

    🃏 **Flashcards**  
    Quickly review key concepts, terminology and facts.

    📝 **Mock FYA**  
    Practise answering longer-form FYA-style questions.

    📊 **Progress**  
    Track your performance and identify areas that need
    further revision.
    """
)

st.divider()


# ---------------------------------------------------------
# REVISION AREAS
# ---------------------------------------------------------

st.header("📚 Revision Areas")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🧬 Genomics")
    st.write(
        """
        • Genomics fundamentals  
        • Sequencing technologies  
        • NGS data  
        • Reference genomes
        """
    )

with col2:
    st.subheader("🧪 Analysis")
    st.write(
        """
        • Quality control  
        • Alignment  
        • Variant calling  
        • Variant annotation
        """
    )

with col3:
    st.subheader("🏥 Clinical")
    st.write(
        """
        • Variant interpretation  
        • Cancer genomics  
        • Rare disease  
        • Clinical validation
        """
    )


st.divider()


# ---------------------------------------------------------
# QUICK START
# ---------------------------------------------------------

st.header("🚀 Quick Start")

st.info(
    """
    **New to SeqSense?**

    Start with 📚 Revision and work through the topics in order.

    Once you've revised a topic, test yourself using 🧠 Quiz.

    When you're ready, try a 📝 Mock FYA assessment.
    """
)


# ---------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------

st.sidebar.title("🧬 SeqSense")

st.sidebar.caption(
    "Clinical Bioinformatics FYA Revision"
)

st.sidebar.divider()


# Revision pages
revision_pages = [
    st.Page("views/sequencing.py", title="Sequencing", icon="🧬"),
    st.Page("views/pipelines.py", title="Pipelines", icon="🔗"),
    st.Page("views/validation.py", title="Validation", icon="🧪"),
    st.Page("views/statistics.py", title="Statistics", icon="🏷️"),
    st.Page("views/genomic_fundamentals.py", title="Genomic Fundamentals", icon="🔬"),
]

# Main navigation
pages = {
    "🏠 Home": [
        st.Page("views/home.py", title="Home", icon="🏠"),
    ],
    "📚 Revision": revision_pages,  # now a list, this will work
    "🧠 Assessment": [
        st.Page("views/quiz.py", title="Quiz", icon="🧠"),
        st.Page("views/flashcards.py", title="Flashcards", icon="🃏"),
        st.Page("views/mock_assessment.py", title="Mock FYA", icon="📝"),
    ],
    "📊 Progress": [
        st.Page("views/progress.py", title="Progress", icon="📊"),
    ],
}


# Run navigation
pg = st.navigation(pages)

pg.run()