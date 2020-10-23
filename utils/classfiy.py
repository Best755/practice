from PIL import Image
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.models import load_model
import numpy as np


def predict(img):
    """
    加载模型和模型预测
    主要步骤:
        1.加载模型(请加载你认为的最佳模型)
        2.图片处理
        3.用加载的模型预测图片的类别
    :param img: PIL.Image 对象
    :return: string, 模型识别图片的类别,
            共 'cardboard','glass','metal','paper','plastic','trash' 6 个类别
    """
    img = Image.open(img)
    # 把图片转换成为numpy数组
    img = img.resize((150, 150))
    img = image.img_to_array(img)

    # 加载模型,加载请注意 model_path 是相对路径, 与当前文件同级。
    # 如果你的模型是在 results 文件夹下的 dnn.h5 模型，则 model_path = 'results/dnn.h5'
    model_path = '././temp/knn.h5'
    # try:
    #     # 作业提交时测试用, 请勿删除此部分
    #     model_path = os.path.realpath(__file__).replace('main.py', model_path)
    # except NameError:
    #     model_path = './' + model_path

    # -------------------------- 实现模型预测部分的代码 ---------------------------
    # 加载模型
    model = load_model(model_path)

    # expand_dims的作用是把img.shape转换成(1, img.shape[0], img.shape[1], img.shape[2])
    x = np.expand_dims(img, axis=0)

    # 模型预测
    y = model.predict(x)

    # 获取labels
    labels = {0: '硬纸板', 1: '玻璃', 2: '金属', 3: '纸', 4: '塑料', 5: '一般垃圾'}

    # -------------------------------------------------------------------------
    predict = labels[np.argmax(y)]

    # 返回图片的类别
    if predict == '硬纸板':
        predict = {"type": '硬纸板',
                   "describe": "硬纸板又称板纸。由各种纸浆加工成的、纤维相互交织组成的厚纸页。纸板与纸的区别通常以定量和厚度来区分，一般将定量超过250g/m2、厚度大于0.5mm的称为纸板（另说：一般将厚度大于0.1mm的纸称为纸板。一般定量小于250g/m2被认为是纸，定量250g/m2或以上的被认为是纸板）"}
    elif predict == '硬纸板':
        predict = {"type": "玻璃",
                   "describe": "玻璃是非晶无机非金属材料，一般是用多种无机矿物(如石英砂、硼砂、硼酸、重晶石、碳酸钡、石灰石、长石、纯碱等)为主要原料，另外加入少量辅助原料制成的。它的主要成分为二氧化硅和其他氧化物。 [1]  普通玻璃的化学组成是Na2SiO3、CaSiO3、SiO2或Na2O·CaO·6SiO2等，主要成分是硅酸盐复盐，是一种无规则结构的非晶态固体。广泛应用于建筑物，用来隔风透光，属于混合物。另有混入了某些金属的氧化物或者盐类而显现出颜色的有色玻璃，和通过物理或者化学的方法制得的钢化玻璃等。有时把一些透明的塑料（如聚甲基丙烯酸甲酯）也称作有机玻璃。"}
    elif predict == '金属':
        predict = {"type": "金属",
                   "describe": "纯金属在常温下一般都是固体（汞除外），有金属光泽（即对可见光强烈反射），大多数为电和热的优良导体，有延展性，密度较大，熔点较高。 [1]  地球上的金属资源广泛地存在于地壳和海洋中，除少数很不活泼的金属如金、银等有单质形式存在外，其余都以化合物的形式存在。 [1]  金属在自然界中广泛存在，在生活中应用极为普遍，在现代工业中是非常重要和应用最多的一类物质。"}
    elif predict == '纸':
        predict = {"type": "纸",
                   "describe": "纸 : 纸（纸） zhǐ 用植物纤维制成的薄片，作为写画、印刷书报、包装等。纸张：纸的总称。纸以张计，故称。纸张一般为分：凸版印刷纸、新闻纸、胶版印刷纸、铜版纸、书皮纸、字典纸、拷贝纸、板纸等。"}
    elif predict == "塑料":
        predict = {"type": "塑料",
                   "describe": "塑料是以单体为原料，通过加聚或缩聚反应聚合而成的高分子化合物(macromolecules)，其抗形变能力中等，介于纤维和橡胶之间，由合成树脂及填料、增塑剂、稳定剂、润滑剂、色料等添加剂组成。"}
    else:
        predict = {"type": "一般垃圾", "describe": "多种类型垃圾以外的分类"}
    return predict
