# SQLUser.MR_PhysicalExam

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PhyE_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| ChildQ03DR | - |  |  | SI | Child Reference: Dressings |
| PhyE_CTPhyExam_DR | bigint |  | FK | SI | Des Ref MRCPhyExam |
| PhyE_Childsub | double |  |  | NO | Childsub |
| PhyE_CreationDate | date |  |  | SI | Create Date |
| PhyE_CreationHospital_DR | bigint |  | FK | SI | Des Ref CreationHospital |
| PhyE_CreationTime | time |  |  | SI | Create Time |
| PhyE_CreationUser_DR | bigint |  | FK | SI | Des Ref Create User |
| PhyE_MasterVersion_DR | varchar |  | FK | SI | Des Ref MRPhysicalExam |
| PhyE_RowId | varchar |  |  | NO | - |
| PhyE_Terminology | varchar |  |  | SI | Terminology |
| PhyE_TextRep | varchar |  |  | SI | Text Representation  |
| PhyE_UpdateDate | date |  |  | SI | UpdateDate |
| PhyE_UpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| PhyE_UpdateTime | time |  |  | SI | UpdateTime |
| PhyE_UpdateUser_DR | bigint |  | FK | SI | Des Ref Update SSUser |
| Q01Q1 | - |  |  | SI | IV Access Device |
| Q01Q2 | - |  |  | SI | Location |
| Q01Q3 | - |  |  | SI | Insertion Site Condition |
| Q01Q4 | - |  |  | SI | Days since Insertion or Re-Wire |
| Q01Q5 | - |  |  | SI | Comments |
| Q01Q6 | - |  |  | SI | Line Number |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*