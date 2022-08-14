import math


class EuclideanDistTracker:
    def __init__(self):
        # Lưu trữ vị trí trung tâm của các đối tượng
        self.center_points = {}
        # số ID
        self.id_count = 0


    def update(self, objects_rect): # object_rect là [x,y,h,w] 
        # box và id đối tượng
        objects_bbs_ids = []

        # lấy điểm trung tâm 
        for rect in objects_rect:
            x, y, h, w = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # tìm xem đối tượng đã được phát hiện hay chưa
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])
                if dist < 50:
                    self.center_points[id] = (cx, cy)
                    print(self.center_points)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break

            # đối tượng mới được phát hiện, gắn id cho đối tượng
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        # xóa các điểm trùng lặp không dùng 
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # cập nhật Ids
        self.center_points = new_center_points.copy()
        return objects_bbs_ids



