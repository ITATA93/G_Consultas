# SQLUser.PA_PersonConsultSetConsR

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONSR_ParRef | varchar | PK |  | NO | PA_PersonConsultSetCons Parent Reference |
| CONSR_Childsub | double |  |  | NO | Childsub |
| CONSR_CreateDate | date |  |  | SI | CreateDate |
| CONSR_CreateTime | time |  |  | SI | CreateTime |
| CONSR_CreateUser_DR | bigint |  | FK | SI | Des Ref CreateUser |
| CONSR_DischSum_DR | varchar |  | FK | SI | Des Ref DischSum |
| CONSR_Order_DR | varchar |  | FK | SI | Des Ref Order |
| CONSR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*