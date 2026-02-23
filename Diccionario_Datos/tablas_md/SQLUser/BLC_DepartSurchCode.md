# SQLUser.BLC_DepartSurchCode

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEPSC_RowId | bigint | PK |  | NO | - |
| DEPSC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DEPSC_CreatedDate | date |  |  | SI | Created Date |
| DEPSC_CreatedTime | time |  |  | SI | Created Time |
| DEPSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEPSC_DateFrom | date |  |  | SI | Date From |
| DEPSC_DateTo | date |  |  | SI | Date To |
| DEPSC_FixedAmt | double |  |  | SI | Fixed Amt |
| DEPSC_Perc | double |  |  | SI | % Charge |
| DEPSC_UpdatedDate | date |  |  | SI | Updated Date |
| DEPSC_UpdatedTime | time |  |  | SI | Updated Time |
| DEPSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q07Q1 | - |  |  | SI | Fecha |
| Q07Q2 | - |  |  | SI | Sesión |
| Q07Q3 | - |  |  | SI | Temas abordados |
| Q07Q4 | - |  |  | SI | Acude con acompañante |
| Q07Q5 | - |  |  | SI | Observaciones |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*