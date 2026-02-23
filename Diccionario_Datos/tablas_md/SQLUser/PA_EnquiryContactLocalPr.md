# SQLUser.PA_EnquiryContactLocalPr

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOCPR_ParRef | bigint | PK |  | NO | PA_Extract Parent Reference |
| LOCPR_Childsub | double |  |  | NO | Childsub |
| LOCPR_ContLocalPriority_DR | bigint |  | FK | SI | Des Ref PACContLocalPriority |
| LOCPR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*