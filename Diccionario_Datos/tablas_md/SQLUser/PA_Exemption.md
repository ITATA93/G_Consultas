# SQLUser.PA_Exemption

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EX_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| EX_Childsub | double |  |  | NO | Childsub |
| EX_DateFrom | date |  |  | SI | Date From |
| EX_DateTo | date |  |  | SI | Date To |
| EX_Location_DR | bigint |  | FK | SI | Des Ref Location |
| EX_Number | varchar |  |  | SI | Number |
| EX_Reason | bigint |  |  | SI | Des Ref Reason |
| EX_Remarks | varchar |  |  | SI | Remarks |
| EX_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*