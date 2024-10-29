# coding=utf-8
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from epwDataframe import Epwdata

class EPWEditorApp(object):
    def __init__(self, master):
        self.master = master
        self.master.title("EPW Editor")

        # 设置主窗口的最小大小
        self.master.minsize(300,300)

        # 创建PanedWindow
        self.paned_window = tk.PanedWindow(self.master, orient=tk.HORIZONTAL, sashwidth=10, sashpad=8)
        self.paned_window.pack(expand=True, fill=tk.BOTH)

        # 用于存储EPW数据和DataFrame的变量
        self.or_epw_path = ""
        self.new_epw_path = ""
        self.or_epw = None
        self.new_epw = None
        self.epw_df = None

        # 创建每个面板的小部件
        self.create_csv_pane()
        self.create_rewrite_pane()

    def create_csv_pane(self):
        csv_pane = tk.Frame(self.paned_window)

        tk.Label(csv_pane, text="Save CSV", font=("Arial", 18, 'bold')).pack(pady=10)

        # 上传EPW文件的按钮
        tk.Button(csv_pane, text="Upload EPW", command=self.upload_epw).pack(pady=10)

        # 保存CSV文件的按钮（初始时禁用）
        self.save_csv_button = tk.Button(csv_pane, text="Save CSV", command=self.save_csv, state=tk.DISABLED)
        self.save_csv_button.pack(pady=10)

        # 将面板添加到PanedWindow
        self.paned_window.add(csv_pane)
        self.paned_window.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_rewrite_pane(self):
        rewrite_pane = tk.Frame(self.paned_window)

        tk.Label(rewrite_pane, text="Rewrite EPW", font=("Arial", 18,'bold')).pack(pady=10)

        # 上传CSV文件的按钮
        tk.Button(rewrite_pane, text="Upload CSV", command=self.upload_csv).pack(pady=10)

        # 上传原始EPW文件的按钮
        tk.Button(rewrite_pane, text="Upload Original EPW", command=self.upload_original_epw).pack(pady=10)

        # 重写EPW文件的按钮（初始时禁用）
        self.rewrite_epw_button = tk.Button(rewrite_pane, text="Rewrite EPW", command=self.rewrite_epw, state=tk.DISABLED)
        self.rewrite_epw_button.pack(pady=10)

        # 将面板添加到PanedWindow
        self.paned_window.add(rewrite_pane)
        self.paned_window.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def upload_epw(self):
        try:
            self.or_epw_path = filedialog.askopenfilename(filetypes=[("EPW Files", "*.epw")])
            if self.or_epw_path:
                self.or_epw = Epwdata(self.or_epw_path)
                self.epw_df = self.or_epw.df_from_epw()

                self.save_csv_button.config(state=tk.NORMAL) # 启用save_csv按钮
                messagebox.showinfo("Upload Successful", "EPW file uploaded.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_csv(self):
        try:
            save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if save_path:
                self.epw_df.to_csv(save_path, index=False)
                tk.messagebox.showinfo("Save CSV", "CSV file saved successfully.")

                self.save_csv_button.config(state=tk.DISABLED) # 禁用save_csv按钮

        except Exception as e:
            messagebox.showerror("Error", str(e))


    def upload_csv(self):
        try:
            csv_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
            if csv_path:
                self.epw_df = pd.read_csv(csv_path)
                messagebox.showinfo("Upload CSV", "CSV file uploaded.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def upload_original_epw(self):
        try:
            self.new_epw_path = filedialog.askopenfilename(filetypes=[("EPW Files", "*.epw")])
            if self.new_epw_path:
                self.new_epw = Epwdata(self.new_epw_path)
                self.rewrite_epw_button.config(state=tk.NORMAL) # 启用rewrite按钮
                messagebox.showinfo("Upload Original EPW", "Original EPW file uploaded.")
                pass
            pass

        except Exception as e:
            messagebox.showerror("Error", str(e))
            pass
        pass

    def rewrite_epw(self):
        try:
            if self.new_epw and self.epw_df is not None:
                self.new_epw = self.new_epw.rewrite_epw_from_df(self.epw_df)
                new_epw_path = filedialog.asksaveasfilename(defaultextension=".epw", filetypes=[("EPW Files", "*.epw")])
                if new_epw_path:
                    self.new_epw.save(new_epw_path)
                    messagebox.showinfo("Rewrite EPW", "EPW file rewritten successfully.")
                    self.rewrite_epw_button.config(state=tk.DISABLED) # 禁用rewrite按钮
                    pass
                pass
            pass

        except Exception as e:
                # import traceback
                # error_info = traceback.format_exc()
                # messagebox.showerror("Error", str(e) + "\n" + error_info)
                messagebox.showerror("Error", str(e))
                pass
        pass
    pass


root = tk.Tk()
app = EPWEditorApp(root)
root.mainloop()
