# EPW Editor | EPW 编辑器

EPW Editor is a GUI application for editing and rewriting `.epw` files. `.epw` files are commonly used weather data formats in energy analysis and building performance simulation. This application allows users to convert EPW files to CSV, edit the CSV data, and write it back to a new EPW file.

EPW Editor 是一个用于编辑和重写 `.epw` 文件的 GUI 应用程序。`.epw` 文件是能源分析和建筑性能模拟中常用的气象文件格式。本应用程序允许用户将 EPW 文件转换为 CSV 文件、编辑 CSV 数据，并将其写回到新的 EPW 文件中。

## Features | 特性

- **Upload EPW File**: Upload an `.epw` file and view its data.
- **Save as CSV**: Convert the uploaded EPW file to a `.csv` format and save it.
- **Upload CSV File**: Upload a modified CSV file to update weather data.
- **Rewrite EPW File**: Generate a new `.epw` file using the data from the uploaded CSV file.

- **上传 EPW 文件**：上传 `.epw` 文件并查看其数据。
- **保存为 CSV**：将上传的 EPW 文件转换为 `.csv` 格式并保存。
- **上传 CSV 文件**：可以上传修改后的 CSV 文件以更新气象数据。
- **重写 EPW 文件**：使用上传的 CSV 文件中的数据生成一个新的 `.epw` 文件。

## Installation | 安装

1. Clone the repository:

   克隆项目仓库：

   ```sh
   git clone <repository_url>
   cd epw-editor
   ```

2. Install the required dependencies:

   安装所需依赖：

   ```sh
   pip install -r requirements.txt
   ```

## Usage | 使用方法

1. **Start the Application**:

   **启动应用程序**：

   Run the following command to start the application:

   运行以下命令启动应用程序：

   ```sh
   python epw_editor.py
   ```

2. **Using the Interface**:

   **使用界面**：
   - Click the "Upload EPW" button to select and upload an `.epw` file.
   - Click the "Save CSV" button to save the `.epw` file as a `.csv` file.
   - Click "Upload CSV" to upload a modified `.csv` file.
   - Click the "Rewrite EPW" button to generate and save a new `.epw` file.

   - 点击 "Upload EPW" 按钮选择并上传 `.epw` 文件。
   - 点击 "Save CSV" 按钮将 `.epw` 文件保存为 `.csv` 文件。
   - 点击 "Upload CSV" 上传修改后的 `.csv` 文件。
   - 点击 "Rewrite EPW" 按钮生成并保存新的 `.epw` 文件。

## Notes | 注意事项

- Ensure all necessary Python dependencies are installed.
- EPW files are weather data files, and any modifications may affect the results of building performance simulations.

- 确保安装了所有必要的 Python 依赖包。
- EPW 文件是气象数据文件，任何修改都可能影响建筑性能模拟的结果。

## Contributing | 贡献

Feel free to raise issues or suggestions! If you want to contribute code, please fork this repository, make your changes, and submit a pull request.

欢迎提出问题或建议！如果您想贡献代码，请先 Fork 本仓库，提交您的改动，然后发起 Pull Request。

