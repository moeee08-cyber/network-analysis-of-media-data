import pandas as pd

def transpose_matrix(input_file, output_file):
    # 读取生成的矩阵文件
    matrix = pd.read_excel(input_file, index_col=0)
    
    # 打印原始矩阵以供检查
    print("Original Matrix:")
    print(matrix)
    
    # 转置矩阵
    transposed_matrix = matrix.transpose()
    
    # 打印转置后的矩阵以供检查
    print("Transposed Matrix:")
    print(transposed_matrix)
    
    # 保存转置后的矩阵到新的 Excel 文件
    transposed_matrix.to_excel(output_file)
    print(f"Transposed matrix saved to: {output_file}")

# 使用示例
transpose_matrix(
    input_file='/Users/wumengmeng/Desktop/project-MediaAgenda/two-mode/step1testcode/step2_code_data/exploratory analysis/canada_cecorrelation_matrix_0105.xlsx', 
    output_file='transposed_ce_matrix_canada0105.xlsx'
)
