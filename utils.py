import streamlit as st
import pandas as pd
from database import add_booking, add_resource, get_bookings, get_resources, update_booking_status

def display_booking_form(resources_df):
    with st.form("booking_form"):
        user_name = st.text_input("Your Name")
        resource = st.selectbox("Select Resource", resources_df["name"])
        date = st.date_input("Booking Date")
        submitted = st.form_submit_button("Submit Booking Request")
        if submitted:
            resource_id = resources_df[resources_df["name"] == resource]["id"].values[0]
            add_booking(user_name, resource_id, str(date))
            st.success("Booking request submitted!")

def display_admin_panel():
    st.subheader("📋 All Bookings")
    bookings = get_bookings()
    if bookings.empty:
        st.info("No bookings yet.")
    else:
        st.dataframe(bookings)

        with st.expander("Update Booking Status"):
            booking_ids = bookings["id"].tolist()
            selected_id = st.selectbox("Select Booking ID", booking_ids)
            new_status = st.selectbox("New Status", ["Pending", "Approved", "Declined"])
            if st.button("Update Status"):
                update_booking_status(selected_id, new_status)
                st.success("Booking status updated.")

    st.subheader("➕ Add New Resource")
    with st.form("add_resource_form"):
        name = st.text_input("Resource Name")
        description = st.text_area("Description")
        submitted = st.form_submit_button("Add Resource")
        if submitted:
            add_resource(name, description)
            st.success("Resource added successfully.")