# SQLUser.PA_LetterNok

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NOK_ParRef | bigint | PK |  | NO | PA_Letter Parent Reference |
| NOK_Childsub | double |  |  | NO | Childsub |
| NOK_Nok_DR | varchar |  | FK | SI | Des Ref PANok |
| NOK_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*