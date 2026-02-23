# SQLUser.INC_ItmRcp

**Schema:** SQLUser
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INREC_ParRef | bigint | PK |  | NO | INC_Itm Parent Reference |
| INREC_Amount | double |  |  | SI | Amount (Manufacture cost) |
| INREC_CTUOM_DR | bigint |  | FK | NO | Des Ref to CTUOM |
| INREC_Childsub | double |  |  | NO | Childsub |
| INREC_CreatedDate | date |  |  | SI | Created Date |
| INREC_CreatedTime | time |  |  | SI | Created Time |
| INREC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INREC_Date_Created | date |  |  | SI | Date Created |
| INREC_Date_Updated | date |  |  | SI | Date Updated |
| INREC_Desc | varchar |  |  | SI | Description |
| INREC_ManufInstruction | varchar |  |  | SI | Manufacture Instruction |
| INREC_Manuf_Time | varchar |  |  | SI | Manufacturing Time |
| INREC_Modify | varchar |  |  | SI | Modify |
| INREC_Qty_Manuf | double |  |  | NO | Qty Manufactured |
| INREC_Quar_Time | varchar |  |  | SI | Quarantine Time |
| INREC_Remarks | varchar |  |  | SI | Remarks |
| INREC_RowId | varchar |  |  | NO | - |
| INREC_Sterile | varchar |  |  | SI | Sterile Set |
| INREC_Time_Created | time |  |  | SI | Time Created |
| INREC_Time_Updated | time |  |  | SI | Time Updated |
| INREC_UpdatedDate | date |  |  | SI | Updated Date |
| INREC_UpdatedTime | time |  |  | SI | Updated Time |
| INREC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| INREC_UserCreat_DR | bigint |  | FK | SI | User Creat Des Ref to SSU |
| INREC_User_Updated_DR | bigint |  | FK | SI | User Updated Des Ref to SSU |
| Q65Q1 | - |  |  | SI | Muscle |
| Q65Q2 | - |  |  | SI | Right |
| Q65Q3 | - |  |  | SI | Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*