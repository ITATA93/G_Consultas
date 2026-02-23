# SQLUser.CT_HSRMSearch

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CTHSRM_CPGroup | varchar |  |  | SI | Freetext for Associated Care Provider Group |
| CTHSRM_CPList | varchar |  |  | SI | List of associated care providers  |
| CTHSRM_OtherLogonLoc_DR | varchar |  | FK | SI | Des Ref SS_UserOtherLogonLoc |
| ChildQ161DR | - |  |  | SI | Child Reference: Paediatric Pre-Admission Services |
| Q143Q1 | - |  |  | SI | Name |
| Q143Q2 | - |  |  | SI | Relationship |
| Q143Q3 | - |  |  | SI | Other relationship |
| Q143Q4 | - |  |  | SI | Notified of admission |
| Q143Q5 | - |  |  | SI | Date |
| Q143Q6 | - |  |  | SI | Time |
| Q143Q7 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*