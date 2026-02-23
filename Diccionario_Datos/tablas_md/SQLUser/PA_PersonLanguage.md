# SQLUser.PA_PersonLanguage

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LANG_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| LANG_Childsub | double |  |  | NO | Childsub |
| LANG_Language_DR | bigint |  | FK | SI | Des Ref to CTLAN |
| LANG_RowId | varchar |  |  | NO | - |
| LANG_Use | varchar |  |  | SI | What the language should be used for. |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*