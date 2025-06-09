import streamlit as st
from database import get_all_resources, get_all_bookings, add_booking, update_booking_status, add_resource
from utils import format_booking

st.set_page_config(page_title="Resource Booking App", layout="wide")

st.title("📅 Resource Booking App")

tabs = st.tabs(["User", "Admin"])

# User Tab
with tabs[0]:
    st.header("Book a Resource")
    resources = get_all_resources()
    if resources:
        resource_names = [r[1] for r in resources]
        selected = st.selectbox("Select a resource", resource_names)
        user_name = st.text_input("Your name")
        if st.button("Request Booking"):
            resource_id = [r[0] for r in resources if r[1] == selected][0]
            add_booking(user_name, resource_id)
            st.success("Booking request submitted!")

    st.subheader("Your Bookings")
    if user_name:
        bookings = get_all_bookings()
        user_bookings = [b for b in bookings if b[1] == user_name]
        for b in user_bookings:
            st.info(format_booking(b))

# Admin Tab
with tabs[1]:
    st.header("Manage Bookings")
    bookings = get_all_bookings()
    if bookings:
        for b in bookings:
            st.write(format_booking(b))
            new_status = st.selectbox("Update status", ["Pending", "Approved", "Declined"], index=["Pending", "Approved", "Declined"].index(b[4]), key=b[0])
            if st.button("Update", key=f"update_{b[0]}"):
                update_booking_status(b[0], new_status)
                st.success("Status updated.")

    st.header("Add New Resource")
    new_resource = st.text_input("Resource name")
    if st.button("Add Resource"):
        add_resource(new_resource)
        st.success("Resource added.")
