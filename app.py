import streamlit as st
import pandas as pd
from database import init_db, get_resources, get_bookings, add_booking, add_resource, update_booking_status
from utils import display_booking_form, display_admin_panel

# Initialize database
init_db()

st.set_page_config(page_title="FENZ CRM Resource Booking System", layout="wide")

st.title("📅 FENZ Resource Booking System")

tabs = st.tabs(["User Booking", "Admin Panel"])

with tabs[0]:
    st.header("Book a Resource")
    resources = get_resources()
    if resources.empty:
        st.info("No resources available. Please contact admin.")
    else:
        display_booking_form(resources)

with tabs[1]:
    st.header("Admin Panel")
    display_admin_panel()
