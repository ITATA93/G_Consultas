# SQLUser.OE_TextResultPictures

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PIC_ParRef | bigint | PK |  | NO | OE_TextResult Parent Reference |
| ChildQ46DR | - |  |  | SI | Child Reference: Muscle Power |
| PIC_Childsub | double |  |  | NO | Childsub |
| PIC_DateCreated | date |  |  | SI | Date Created |
| PIC_Desc | varchar |  |  | SI | Description |
| PIC_DocSubType_DR | bigint |  | FK | SI | Des Ref DocSubType |
| PIC_DocType_DR | bigint |  | FK | SI | des ref to PAC_DocumentType |
| PIC_Path | varchar |  |  | SI | Path |
| PIC_RowId | varchar |  |  | NO | - |
| PIC_TimeCreated | time |  |  | SI | Time Created |
| PIC_UpdateDate | date |  |  | SI | UpdateDate |
| PIC_UpdateTime | time |  |  | SI | UpdateTime |
| PIC_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| PIC_UserCreated | bigint |  |  | SI | User Created |
| PIC_websysDocument | bigint |  |  | SI | websysDocument |
| Q42Q1 | - |  |  | SI | Joint / Motion |
| Q42Q2 | - |  |  | SI | AROM left |
| Q42Q3 | - |  |  | SI | PROM left |
| Q42Q4 | - |  |  | SI | AROM right |
| Q42Q5 | - |  |  | SI | PROM right |
| Q42Q6 | - |  |  | SI | End feel |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*