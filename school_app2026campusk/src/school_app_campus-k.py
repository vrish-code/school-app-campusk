import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import random
import os
import string as s

wsimgpath = r"school_app2026campusk/src/Ws.png"
st.set_page_config(layout="wide")
st.set_page_config(initial_sidebar_state="expanded")
fpj = r"school_app2026campusk/src/1.png"
fpf = r"school_app2026campusk/src/2.png"
fpm = r"school_app2026campusk/src/3.png"
fpa = r"school_app2026campusk/src/4.png"
fpma = r"school_app2026campusk/src/5.png"
fpju = r"school_app2026campusk/src/6.png"
fpjul = r"school_app2026campusk/src/7.png"
fpau = r"school_app2026campusk/src/8.png"
fpsep = r"school_app2026campusk/src/9.png"
fpo = r"school_app2026campusk/src/10.png"
fpn = r"school_app2026campusk/src/11.png"
fpd = r"school_app2026campusk/src/12.png"

WS1 = {
    "Path": r"school_app2026campusk/src/Worksheet_1.pdf",
    "Subject": "Math and Science",
    "Date issued": f"{random.randint(1,30)}/{random.randint(3,12)}/{random.randint(2020, 2026)}",
}
WS2 = {
    "Path": r"school_app2026campusk/src/Worksheet_2.pdf",
    "Subject": "Mixed subjects",
    "Date issued": f"{random.randint(1,30)}/{random.randint(3,12)}/{random.randint(2020, 2026)}",
}

Announcements = [
    "Pay tuition fees by March 15th\n",
    "Tomorrow is a holiday - Holi festival\n",
    "PTM for parents on Saturday 9 AM\n",
    "Science fair registration closes Friday\n",
    "Library books due by March 12th\n",
    "Sports day practice starts Monday\n",
    "Uniform cleaning service available\n",
    "Math Olympiad team selection tomorrow\n",
    "Not paid school on March 18th - Annual Day prep\n",
    "Stationery shop open after school hours\n",
    "Exam fees due by March 20th\n",
    "Computer lab timings changed to 3-5 PM\n",
    "Lost & Found items at admin office\n",
    "Basketball trials for under-14 team\n",
    "Class photo session on Friday morning\n",
]


Data = {}
Msgs = []
calendar = {
    "January": {
        "Mondays": [5, 12, 19, 26],
        "Tuesdays": [6, 13, 20, 27],
        "Wednesdays": [7, 14, 21, 28],
        "Thursdays": [1, 8, 15, 22, 29],
        "Fridays": [2, 9, 16, 23, 30],
        "Saturdays": [3, 10, 17, 24, 31],
        "Sundays": [4, 11, 18, 25],
    },
    "February": {
        "Mondays": [2, 9, 16, 23],
        "Tuesdays": [3, 10, 17, 24],
        "Wednesdays": [4, 11, 18, 25],
        "Thursdays": [5, 12, 19, 26],
        "Fridays": [6, 13, 20, 27],
        "Saturdays": [7, 14, 21, 28],
        "Sundays": [1, 8, 15, 22],
    },
    "March": {
        "Mondays": [2, 9, 16, 23, 30],
        "Tuesdays": [3, 10, 17, 24, 31],
        "Wednesdays": [4, 11, 18, 25],
        "Thursdays": [5, 12, 19, 26],
        "Fridays": [6, 13, 20, 27],
        "Saturdays": [7, 14, 21, 28],
        "Sundays": [1, 8, 15, 22, 29],
    },
    "April": {
        "Mondays": [6, 13, 20, 27],
        "Tuesdays": [7, 14, 21, 28],
        "Wednesdays": [1, 8, 15, 22, 29],
        "Thursdays": [2, 9, 16, 23, 30],
        "Fridays": [3, 10, 17, 24],
        "Saturdays": [4, 11, 18, 25],
        "Sundays": [5, 12, 19, 26],
    },
    "May": {
        "Mondays": [4, 11, 18, 25],
        "Tuesdays": [5, 12, 19, 26],
        "Wednesdays": [6, 13, 20, 27],
        "Thursdays": [7, 14, 21, 28],
        "Fridays": [1, 8, 15, 22, 29],
        "Saturdays": [2, 9, 16, 23, 30],
        "Sundays": [3, 10, 17, 24, 31],
    },
    "June": {
        "Mondays": [1, 8, 15, 22, 29],
        "Tuesdays": [2, 9, 16, 23, 30],
        "Wednesdays": [3, 10, 17, 24],
        "Thursdays": [4, 11, 18, 25],
        "Fridays": [5, 12, 19, 26],
        "Saturdays": [6, 13, 20, 27],
        "Sundays": [7, 14, 21, 28],
    },
    "July": {
        "Mondays": [6, 13, 20, 27],
        "Tuesdays": [7, 14, 21, 28],
        "Wednesdays": [1, 8, 15, 22, 29],
        "Thursdays": [2, 9, 16, 23, 30],
        "Fridays": [3, 10, 17, 24, 31],
        "Saturdays": [4, 11, 18, 25],
        "Sundays": [5, 12, 19, 26],
    },
    "August": {
        "Mondays": [3, 10, 17, 24, 31],
        "Tuesdays": [4, 11, 18, 25],
        "Wednesdays": [5, 12, 19, 26],
        "Thursdays": [6, 13, 20, 27],
        "Fridays": [7, 14, 21, 28],
        "Saturdays": [1, 8, 15, 22, 29],
        "Sundays": [2, 9, 16, 23, 30],
    },
    "September": {
        "Mondays": [7, 14, 21, 28],
        "Tuesdays": [1, 8, 15, 22, 29],
        "Wednesdays": [2, 9, 16, 23, 30],
        "Thursdays": [3, 10, 17, 24],
        "Fridays": [4, 11, 18, 25],
        "Saturdays": [5, 12, 19, 26],
        "Sundays": [6, 13, 20, 27],
    },
    "October": {
        "Mondays": [5, 12, 19, 26],
        "Tuesdays": [6, 13, 20, 27],
        "Wednesdays": [7, 14, 21, 28],
        "Thursdays": [1, 8, 15, 22, 29],
        "Fridays": [2, 9, 16, 23, 30],
        "Saturdays": [3, 10, 17, 24, 31],
        "Sundays": [4, 11, 18, 25],
    },
    "November": {
        "Mondays": [2, 9, 16, 23, 30],
        "Tuesdays": [3, 10, 17, 24],
        "Wednesdays": [4, 11, 18, 25],
        "Thursdays": [5, 12, 19, 26],
        "Fridays": [6, 13, 20, 27],
        "Saturdays": [7, 14, 21, 28],
        "Sundays": [1, 8, 15, 22, 29],
    },
    "December": {
        "Mondays": [7, 14, 21, 28],
        "Tuesdays": [1, 8, 15, 22, 29],
        "Wednesdays": [2, 9, 16, 23, 30],
        "Thursdays": [3, 10, 17, 24, 31],
        "Fridays": [4, 11, 18, 25],
        "Saturdays": [5, 12, 19, 26],
        "Sundays": [6, 13, 20, 27],
    },
}


names = [
    "Aarav Sharma",
    "Priya Patel",
    "Rohit Kumar",
    "Anjali Singh",
    "Arjun Reddy",
    "Neha Gupta",
    "Vikram Desai",
    "Divya Iyer",
    "Siddharth Joshi",
    "Riya Nair",
    "Karan Yadav",
    "Pooja Mishra",
    "Nikhil Rao",
    "Shruti Menon",
    "Aditya Jain",
    "Kavya Pillai",
    "Rajesh Patel",
    "Meera Bose",
    "Sahil Verma",
    "Nisha Khan",
    "Aryan Chauhan",
    "Sanya Malhotra",
    "Devansh Pawar",
    "Isha Agarwal",
    "Kunal Das",
    "Tara Sethi",
    "Manish Thakur",
    "Lakshmi Sahu",
    "Rohan Bhatt",
    "Swati Dubey",
    "Vishal Pandey",
    "Radha Tripathi",
    "Sameer Saxena",
    "Deepika Roy",
    "Akshay Negi",
    "Aishwarya Rana",
    "Prateek Solanki",
    "Nidhi Rawat",
    "Harsh Bansal",
    "Sneha Puri",
    "Gaurav Tyagi",
    "Payal Chauhan",
    "Yashwant Koli",
    "Riddhi Sharma",
    "Abhay Mehra",
    "Tanvi Kapoor",
    "Rishi Bakshi",
    "Kiara Lobo",
    "Saurabh Nanda",
    "Mahi Sawant",
    "Jai Ganesh",
    "Simran Kaur",
]
classes = classes_sections = [
    "6A",
    "6B",
    "6C",
    "7A",
    "7B",
    "7C",
    "8A",
    "8B",
    "8C",
    "9A",
    "9B",
    "9C",
    "10A",
    "10B",
    "10C",
    "5A",
    "5B",
    "11A",
    "11B",
    "12A",
    "12B",
]
school = "Example CBSE School"


def init():
    stud = {
        "Name": random.choice(names),
        "Class": random.choice(classes),
        "Roll No": random.choice(list(range(1, 40))),
        "School": school,
        "Attendance": {
            "January 2026": [
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                True,
            ],
            "February 2026": [
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
            ],
            "March 2026": [
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
            ],
            "April 2026": [
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
            ],
            "May 2026": [
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
            ],
            "June 2026": [
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
            ],
            "July 2026": [
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
            ],
            "August 2026": [
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                True,
            ],
            "September 2026": [
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                False,
            ],
            "October 2026": [
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                True,
            ],
            "November 2026": [
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
            ],
            "December 2026": [
                False,
                True,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                True,
            ],
        },
        "Marks": {
            "UT1": {
                "Math": 49,
                "Sci": 50,
                "Eng": 43,
                "IIIL": 48,
                "IIL": 47,
                "SST": 46,
                "Total marks per exam": 50,
                "Total score": 283,
                "Total possible score": 50 * 6,
                "Percentage": 283 / 300 * 100,
            },
            "UT2": {
                "Math": 49,
                "Sci": 50,
                "Eng": 43,
                "IIIL": 48,
                "IIL": 47,
                "SST": 46,
                "Total marks per exam": 50,
                "Total score": 283,
                "Total possible score": 50 * 6,
                "Percentage": 283 / 300 * 100,
            },
            "T1": {
                "Math": 100,
                "Sci": 97,
                "Eng": 99,
                "IIIL": 94,
                "IIL": 90,
                "SST": 100,
                "Total score": 100 + 97 + 99 + 94 + 90 + 100,
                "Total marks per exam": 100,
                "Total possible score": 100 * 6,
                "Percentage": 580 / 600 * 100,
            },
        },
    }
    Data.clear()
    Data.update(stud)


def att():
    st.title("Attendance 📋")
    j = fe = m = a = ma = ju = jul = aug = sep = o = n = d = 0
    for f in Data["Attendance"]:
        j = sum(1 for x in Data["Attendance"]["January 2026"] if x == True)
        fe = sum(1 for y in Data["Attendance"]["February 2026"] if y == True)
        m = sum(1 for z in Data["Attendance"]["March 2026"] if z == True)
        a = sum(1 for l in Data["Attendance"]["April 2026"] if l == True)
        ma = sum(1 for m in Data["Attendance"]["May 2026"] if m == True)
        ju = sum(1 for a in Data["Attendance"]["June 2026"] if a == True)
        jul = sum(1 for b in Data["Attendance"]["July 2026"] if b == True)
        aug = sum(1 for c in Data["Attendance"]["August 2026"] if c == True)
        sep = sum(1 for k in Data["Attendance"]["September 2026"] if k == True)
        o = sum(1 for _ in Data["Attendance"]["October 2026"] if _ == True)
        n = sum(1 for h in Data["Attendance"]["November 2026"] if h == True)
        d = sum(1 for i in Data["Attendance"]["December 2026"] if i == True)

    attendance = [j, fe, m, a, ma, ju, jul, aug, sep, o, n, d]
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    dm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    apd = {}
    for i in range(12):
        apd[months[i]] = (attendance[i] / dm[i]) * 100
    apddf = pd.DataFrame(
        list(apd.items()), columns=["Month", "Attendance in percentage"]
    )
    st.subheader(f"Attendance of {Data["Name"]}")
    st.dataframe(apddf)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        b, a = plt.subplots()
        a.grid(True, which='major', axis='both', alpha=0.3, linestyle='--')
        a.bar(
            [months[3], months[5], months[8], months[10]],
            [attendance[3], attendance[5], attendance[8], attendance[10]],
            color="skyblue",
        )
        a.set_title(f"Attendance of {Data["Name"]}–months with 30 days")
        a.set_xlabel("Months")
        a.set_ylabel("Attendance out of 30 days")
        a.set_ylim(0, 30)
        
        st.pyplot(b)
        plt.close(b)
    with c2:
        c, d = plt.subplots()
        d.bar(
            [
                months[0],
                months[2],
                months[4],
                months[6],
                months[7],
                months[9],
                months[11],
            ],
            [
                attendance[0],
                attendance[2],
                attendance[4],
                attendance[6],
                attendance[7],
                attendance[9],
                attendance[11],
            ],
            color="skyblue",
        )
        d.grid(True, which='major', axis='both', alpha=0.3, linestyle='--')
        d.set_title(f"Attendance of {Data["Name"]}—months with 31 days")
        d.set_xlabel("Months")
        d.set_ylabel("Attendance out of 31 days")
        d.set_ylim(0, 31)
        st.pyplot(c)
        plt.close(c)
    with c3:
        e, f = plt.subplots()
        f.grid(True, which='major', axis='both', alpha=0.3, linestyle='--')
        f.bar([months[1]], [attendance[1]], color="skyblue")
        f.set_title(f"Attendance of {Data["Name"]}—month with 28 days (February)")
        f.set_xlabel("Month")
        f.set_ylabel("Attendance out of 28 days")
        f.set_ylim(0, 31)
        st.pyplot(e)
        plt.close(e)
    with c4:
        g, h = plt.subplots()
        h.grid(True, which='major', axis='both', alpha=0.3, linestyle='--')
        h.bar(["Total attendance"], [sum(attendance) / sum(dm) * 100], color="skyblue")
        h.set_title(f"Attendance of {Data["Name"]}—total")
        h.set_xlabel("Total attendance percentage")
        h.set_ylabel("Percentage")
        h.set_ylim(0, 100)
        h.grid(True, alpha=0.06, linestyle="--")
        st.pyplot(g)
        plt.close(g)


def profile():
    st.subheader("Profile")
    st.image(r"school_app2026campusk/src/pfp.png")
    pfdict = {
        "Name": Data["Name"],
        "Class": Data["Class"],
        "Roll No": Data["Roll No"],
        "School": Data["School"],
    }
    dfpf = pd.DataFrame(list(pfdict.items()), columns=["Student Details", "Status"])
    st.dataframe(dfpf)


def markss():
    mut = list(Data["Marks"]["UT1"].values())[:-4]
    mt = list(Data["Marks"]["T1"].values())[:-4]
    utdf = pd.DataFrame(
        list(Data["Marks"]["UT1"].items()), columns=["Subjects", "Marks"]
    )
    st.image(r"school_app2026campusk/src/pfp.png")
    pfdict = {
        "Name": Data["Name"],
        "Class": Data["Class"],
        "Roll No": Data["Roll No"],
        "School": Data["School"],
    }
    dfpf = pd.DataFrame(list(pfdict.items()), columns=["Student Details", "Status"])
    st.dataframe(dfpf)
    ut2df = pd.DataFrame(
        list(Data["Marks"]["UT2"].items()), columns=["Subjects", "Marks"]
    )
    tdf = pd.DataFrame(list(Data["Marks"]["T1"].items()), columns=["Subjects", "Marks"])
    subjects = list(Data["Marks"]["UT1"].keys())[:-4]
    etc = {
        "UT1": {"Taken score": 283, "Out of": 300},
        "UT2": {"Taken score": 283, "Out of": 300},
        "T1": {"Taken score": 580, "Out of": 600},
    }

    etcdf = pd.DataFrame(list(etc.items()), columns=["Exam", "Marks"])
    t1, t2, t3, t4 = st.tabs(["UT1", "UT2", "T1", "Total scores"])
    with t1:
        st.subheader("UT1 performance")
        st.dataframe(utdf)
        f, a = plt.subplots()
        a.grid(True, which='major', axis='both', alpha=0.3, linestyle='--')
        a.bar(subjects, mut, color="skyblue")
        a.set_title("UT1 performance")
        a.set_xlabel("Subjects")
        a.set_ylabel("Marks")
        a.set_ylim(0, 50)
       
        st.pyplot(f)
        plt.close(f)
    with t2:
        st.subheader("UT2 performance")
        st.dataframe(ut2df)
        f, a = plt.subplots()
        a.grid(True, which='major', axis='both', alpha=0.3, linestyle='--')
        a.bar(subjects, mut, color="skyblue")
        a.set_title("UT2 performance")
        a.set_xlabel("Subjects")
        a.set_ylabel("Marks")
        a.set_ylim(0, 50)
        
        st.pyplot(f)
        plt.close(f)
    with t3:
        st.subheader("T1 performance")
        st.dataframe(tdf)
        f, a = plt.subplots()
        a.grid(True, which='major', axis='both', alpha=0.3, linestyle='--')
        a.bar(subjects, mt, color="skyblue")
        a.set_title("T1 performance")
        a.set_xlabel("Subjects")
        a.set_ylabel("Marks")
        a.set_ylim(0, 100)
        st.pyplot(f)
        plt.close(f)
    with t4:
        st.subheader("Total performance")
        st.dataframe(etcdf)
        c1, c2 = st.columns(2)
        with c1:
            f, a = plt.subplots()
            a.grid(True, which='major', axis='both', alpha=0.3, linestyle='--')
            a.bar(["UT1", "UT2"], [283, 283], color="skyblue")
            a.set_title("Overall performance")
            a.set_xlabel("Exams")
            a.set_ylabel("Marks")
            a.set_ylim(0, 300)
            st.pyplot(f)
            plt.close(f)
        with c2:
            f, a = plt.subplots()
            a.grid(True, which='major', axis='both', alpha=0.3, linestyle='--')
            a.bar(["T1"], [580], color="skyblue")
            a.set_title("Overall performance")
            a.set_xlabel("Exam")
            a.set_ylabel("Marks")
            a.set_ylim(0, 600)
            st.pyplot(f)
            plt.close(f)


def MSG():
    st.write("Write to School 📝")
    with st.form(key="WTS"):
        msg = st.text_area(label="Enter your message.")
        submit = st.form_submit_button("Submit")
    if submit:
        st.toast("Message submitted!")
        Msgs.append({"Message 1": msg})
        st.write(Msgs)
        s = st.selectbox("Want to write another message?", ["Paid", "Not paid"])
        if s == "Paid":
            st.rerun()
        elif s == "Not paid":
            pass


def announcement():
    st.title("Announcements 📢")
    for a in range(len(Announcements)):
        st.write(
                f"""⚠️ Announcement ⚠️\n
                    {Announcements[a]}\n
                    """
            )


def calendar2026():
    st.title("Calendar 🗓️")
    mo = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    d = [
        "Mondays",
        "Tuesdays",
        "Wednesdays",
        "Thursdays",
        "Fridays",
        "Saturdays",
        "Sundays",
    ]
    t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12 = st.tabs(mo)
    s = ""
    with t1:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[0])
            st.write(f"{d[0]}:{calendar[mo[0]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[0]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[0]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[0]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[0]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[0]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[0]][d[6]]}")
        with c2:
            st.image(fpj)
    with t2:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[1])
            st.write(f"{d[0]}:{calendar[mo[1]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[1]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[1]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[1]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[1]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[1]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[1]][d[6]]}")
        with c2:
            st.image(fpf)
    with t3:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[2])
            st.write(f"{d[0]}:{calendar[mo[2]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[2]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[2]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[2]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[2]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[2]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[2]][d[6]]}")
        with c2:
            st.image(fpm)
    with t4:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[3])
            st.write(f"{d[0]}:{calendar[mo[3]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[3]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[3]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[3]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[3]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[3]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[3]][d[6]]}")
        with c2:
            st.image(fpa)
    with t5:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[4])
            st.write(f"{d[0]}:{calendar[mo[4]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[4]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[4]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[4]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[4]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[4]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[4]][d[6]]}")
        with c2:
            st.image(fpma)
    with t6:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[5])
            st.write(f"{d[0]}:{calendar[mo[5]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[5]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[5]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[5]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[5]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[5]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[5]][d[6]]}")
        with c2:
            st.image(fpju)
    with t7:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[6])
            st.write(f"{d[0]}:{calendar[mo[6]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[6]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[6]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[6]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[6]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[6]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[6]][d[6]]}")
        with c2:
            st.image(fpjul)
    with t8:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[7])
            st.write(f"{d[0]}:{calendar[mo[7]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[7]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[7]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[7]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[7]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[7]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[7]][d[6]]}")
        with c2:
            st.image(fpau)
    with t9:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[8])
            st.write(f"{d[0]}:{calendar[mo[8]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[8]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[8]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[8]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[8]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[8]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[8]][d[6]]}")
        with c2:
            st.image(fpsep)
    with t10:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[9])
            st.write(f"{d[0]}:{calendar[mo[9]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[9]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[9]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[9]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[9]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[9]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[9]][d[6]]}")
        with c2:
            st.image(fpo)
    with t11:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[10])
            st.write(f"{d[0]}:{calendar[mo[10]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[10]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[10]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[10]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[10]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[10]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[10]][d[6]]}")
        with c2:
            st.image(fpn)
    with t12:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(mo[11])
            st.write(f"{d[0]}:{calendar[mo[11]][d[0]]}")
            st.write(f"{d[1]}:{calendar[mo[11]][d[1]]}")
            st.write(f"{d[2]}:{calendar[mo[11]][d[2]]}")
            st.write(f"{d[3]}:{calendar[mo[11]][d[3]]}")
            st.write(f"{d[4]}:{calendar[mo[11]][d[4]]}")
            st.write(f"{d[5]}:{calendar[mo[11]][d[5]]}")
            st.write(f"{d[6]}:{calendar[mo[11]][d[6]]}")
        with c2:
            st.image(fpd)


def pay():
    if "Payments" not in st.session_state:
        st.session_state.Payments = {
            "Payments_2026": {
                "Tuition (15000)": "Not paid",
                "Van (15000)": "Not paid",
                "Lab (15000)": "Not paid",
                "Annual charges (15000)": "Not paid",
            },
            "Payments_2027": {
                "Tuition (15000)": "Not paid",
                "Van (15000)": "Not paid",
                "Lab (15000)": "Not paid",
                "Annual charges (15000)": "Not paid",
            },
            "Payments_2028": {
                "Tuition (15000)": "Not paid",
                "Van (15000)": "Not paid",
                "Lab (15000)": "Not paid",
                "Annual charges (15000)": "Not paid",
            },
        }
    st.title("Payments 💵")
    paydf2026 = pd.DataFrame(
        list(st.session_state.Payments["Payments_2026"].items()),
        columns=["Payment", "Status"],
    )
    paydf2027 = pd.DataFrame(
        list(st.session_state.Payments["Payments_2027"].items()),
        columns=["Payment", "Status"],
    )
    paydf2028 = pd.DataFrame(
        list(st.session_state.Payments["Payments_2028"].items()),
        columns=["Payment", "Status"],
    )
    t1, t2, t3 = st.tabs(["Payments-2026 💵", "Payments-2027 💵", "Payments-2028 💵"])
    with t1:
        st.subheader("Payments 2026")
        st.dataframe(paydf2026)
        if st.button("Pay all 💵", key="2026"):
            for p in st.session_state.Payments["Payments_2026"]:
                st.session_state.Payments["Payments_2026"][p] = "Paid"
            paydf2026 = pd.DataFrame(
        list(st.session_state.Payments["Payments_2026"].items()),
        columns=["Payment", "Status"],
    )
            st.dataframe(paydf2026)
            st.toast(f"You paid all the fees for {Data["Name"]}!")
            st.balloons()
          

            

    with t2:
        st.subheader("Payments 2027")
        st.dataframe(paydf2027)
        if st.button("Pay all 💵", key="2027"):
            for p in st.session_state.Payments["Payments_2027"]:
                st.session_state.Payments["Payments_2027"][p] = "Paid"
            paydf2027 = pd.DataFrame(
        list(st.session_state.Payments["Payments_2027"].items()),
        columns=["Payment", "Status"],
    )
            st.dataframe(paydf2027)
            st.toast(f"You paid all the fees for {Data["Name"]}!")
            st.balloons()
            
    with t3:
        st.subheader("Payments 2028")
        st.dataframe(paydf2028)
        if st.button("Pay all 💵", key="2028"):
            for p in st.session_state.Payments["Payments_2028"]:
                st.session_state.Payments["Payments_2028"][p] = "Paid"
            paydf2028 = pd.DataFrame(
        list(st.session_state.Payments["Payments_2028"].items()),
        columns=["Payment", "Status"],
    )  
            st.dataframe(paydf2028)
            st.toast(f"You paid all the fees for {Data["Name"]}!")
            st.balloons()
          

def hw():
    st.title("Homework--There are 2 worksheets to be downloaded.")
    t1, t2 = st.tabs(["WS1", "WS2"])
    with t1:
        c1, c2 = st.columns(2)
        with c1:
            with open(WS1["Path"], "rb") as f:
                st.write("\tWorksheet 1\t")
                st.write(f"Subject: {WS1["Subject"]}")
                st.write(f"Date issued: {WS1["Date issued"]}")
                st.download_button(
                    label="📄Download Worksheet 1",
                    data=f.read(),
                    file_name="Worksheet_1.pdf",
                    mime="application/pdf",
                )

        with c2:
            st.image(wsimgpath)

    with t2:
        c1, c2 = st.columns(2)
        with c1:
            with open(WS2["Path"], "rb") as f:
                st.write("\tWorksheet 2\t")
                st.write(f"Subject: {WS2["Subject"]}")
                st.write(f"Date issued: {WS2["Date issued"]}")
                st.download_button(
                    label="📄Download Worksheet 2",
                    data=f.read(),
                    file_name="Worksheet_2.pdf",
                    mime="application/pdf",
                )
        with c2:
            st.image(wsimgpath)


def notifications():
    st.title("Check notifications.")
    if st.button("Check notifications"):
        st.toast("🚨 Fee due tomorrow!")
        st.toast("⚠️ Math test today!")
        st.toast(
            f"📋PTM scheduled on {random.randint(1,11)}/{random.randint(1,11)}/{random.randint(2020, 2026)} "
        )


init()
with st.sidebar:
    c = st.selectbox(
        "Choose to view or do:",
        [
            "Check announcement 📢",
            "Attendance 📋",
            "Marks 📊🥇",
            "Profile 👤",
            "Homework 📚",
            "Write to school📝",
            "Check notifications ⚠️",
            "Check Payments 💵",
            "View calendar 🗓️",
        ],
    )
match c:
    case "Check announcement 📢":
        announcement()
    case "Attendance 📋":
        att()
    case "Marks 📊🥇":
        markss()
    case "Profile 👤":
        profile()
    case "Homework 📚":
        hw()
    case "Write to school📝":
        MSG()
    case "Check notifications ⚠️":
        notifications()
    case "Check Payments 💵":
        pay()
    case "View calendar 🗓️":
        calendar2026()
