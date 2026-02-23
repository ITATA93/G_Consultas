# SQLUser.MR_ReviewOfSystems

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROS_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| Q35Q1 | - |  |  | SI | Administration Date: |
| Q35Q2 | - |  |  | SI | Administration Time: |
| Q35Q3 | - |  |  | SI | Results (mmol/L) |
| Q35Q4 | - |  |  | SI | Dose (Units): |
| Q35Q5 | - |  |  | SI | Executed by: |
| Q35Q6 | - |  |  | SI | Overseer: |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| ROS_CTROS_DR | bigint |  | FK | SI | Des Ref MRCReviewOfSystem |
| ROS_Childsub | double |  |  | NO | Childsub |
| ROS_CreationDate | date |  |  | SI | Create Date |
| ROS_CreationHospital_DR | bigint |  | FK | SI | Des Ref CreationHospital |
| ROS_CreationTime | time |  |  | SI | Create Time |
| ROS_CreationUser_DR | bigint |  | FK | SI | Des Ref Create User |
| ROS_MasterVersion_DR | varchar |  | FK | SI | Des Ref MRReviewOfSystems |
| ROS_RowId | varchar |  |  | NO | - |
| ROS_Terminology | varchar |  |  | SI | Terminology |
| ROS_TextRep | varchar |  |  | SI | Text Representation  |
| ROS_UpdateDate | date |  |  | SI | UpdateDate |
| ROS_UpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| ROS_UpdateTime | time |  |  | SI | UpdateTime |
| ROS_UpdateUser_DR | bigint |  | FK | SI | Des Ref Update SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*