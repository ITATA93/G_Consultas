# SQLUser.PA_EnquiryContactServProv

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SERPR_ParRef | bigint | PK |  | NO | PA_Extract Parent Reference |
| ChildQ09DR | - |  |  | SI | Child Reference: Equipamiento_old |
| Q45Q1 | - |  |  | SI | Empresa Externa |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SERPR_Childsub | double |  |  | NO | Childsub |
| SERPR_ContServiceProvided_DR | bigint |  | FK | SI | Des Ref PACContServiceProvided |
| SERPR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*