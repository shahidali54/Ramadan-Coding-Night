# Import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available timezones.
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# App title
st.title("⏰ Time Zone App")

# Create a multiselect widget for selecting timezones
selected_time_zone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC","Asia/Karachi"])

# Display the selected timezones in a subheader
st.subheader("Selected Timezone(s):")
for tz in selected_time_zone:

    # Get and format current time for each selected timezone with AM/PM format
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    # Display the current time for each selected timezone
    st.write(f"**{tz}**: {current_time}")

# Create a subheader for converting time between timezones
st.subheader("Convert Time Between Timezones")

# create a time input widget for the current time
current_time = st.time_input("Current Time", value=datetime.now().time())

# Creat a select box for selecting the timezones to convert from
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

# Create a select box for selecting the timezones to convert to
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Create a button to trigger the time conversion
if st.button("Convert Time"):

    # Combine the current time with the selected time zone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))

    # Convert the time to the selected timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %M:%S %p")

    # Display the converted time in the selected timezone
    st.success(f"Converted Time in {to_tz}: {converted_time}")

    st.write("---------------------------------")

st.write("Build with ❤️ by [Shahid Ali]")
